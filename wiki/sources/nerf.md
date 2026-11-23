---
id: src-nerf
type: source
title: "NeRF: Representing Scenes as Neural Radiance Fields for View Synthesis"
authors: Mildenhall, Srinivasan, Tancik, Barron, Ramamoorthi, Ng
venue: ECCV 2020
raw: raw/nerf_2003.08934.pdf
arxiv: https://arxiv.org/abs/2003.08934
---

# NeRF（Mildenhall et al., 2020）

## 一句話
把整個場景存成一個神經網路函數：輸入「空間位置 + 觀看方向」，輸出「顏色 + 密度」，再用體渲染把它畫成照片。

## 解決什麼問題
[[novel-view-synthesis]]：只給一組**已知相機位姿**的照片，合成任意新視角的照片。

## 核心方法
1. **場景表示**：MLP `F(x, d) → (c, σ)`。
   - 輸入 5D：位置 `x=(x,y,z)` + 方向 `(θ,φ)`（實作上用 3D 單位向量 d）。
   - 輸出：RGB 顏色 `c` 與體密度 `σ`。
   - 網路：8 層全連接（ReLU、256 channels）先處理位置，輸出 σ 與 256 維特徵；再接上方向，經 1 層（128 channels）輸出 RGB。（論文 Sec. 3）
   - **σ 只依賴位置、顏色才依賴方向** → 保證多視角幾何一致，又能表現反光（non-Lambertian）。
2. **體渲染**：沿每條相機光線取樣點，用 [[volume-rendering]] 公式累積顏色；此過程可微分。
3. **Positional encoding**：把座標映射到高頻 sin/cos，位置用 L=10、方向用 L=4。（Sec. 5.1）見 [[positional-encoding]]
4. **階層式取樣**：coarse 網路每條光線 Nc=64 點，fine 網路再加 Nf=128 點，把樣本集中在有東西的地方。（Sec. 5.2）
5. **訓練**：最小化渲染圖與真實照片的平方誤差；batch 4096 條光線。

## 關鍵數字
| 項目 | 數值 | 出處 |
|---|---|---|
| 訓練時間 | 100–300k iterations，單張 V100 約 1–2 天 | Sec. 5.3 |
| 渲染時間 | 約 30 秒 / 張（V100） | Appendix |

## 意義與限制
- 第一個能從真實照片渲染出高解析、照片級新視角的連續神經場景表示（作者自述）。
- 儲存小（只有網路權重），但**每個像素要查詢 MLP 上百次** → 訓練、渲染都很慢。這成為後續 [[src-plenoxels]]、[[src-instant-ngp]]、[[src-3dgs]] 的出發點。
- 輸出是一個**隱式**的輻射場，不是 mesh。見 [[implicit-vs-explicit]]

## 相關概念
[[radiance-field]] · [[volume-rendering]] · [[positional-encoding]] · [[sfm-camera-pose]]
