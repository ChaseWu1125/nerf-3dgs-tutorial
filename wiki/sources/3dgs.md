---
id: src-3dgs
type: source
title: "3D Gaussian Splatting for Real-Time Radiance Field Rendering"
authors: Kerbl, Kopanas, Leimkühler, Drettakis
venue: SIGGRAPH 2023 (ACM TOG 42(4))
raw: raw/3dgs_2308.04079.pdf
arxiv: https://arxiv.org/abs/2308.04079
---

# 3D Gaussian Splatting（Kerbl et al., 2023）

## 一句話
用幾百萬顆有顏色、半透明、可拉伸旋轉的 3D 橢圓（高斯）來表示場景，直接「拍扁」到畫面上光柵化，所以能 1080p 即時渲染。

## 三個關鍵元件（論文 Abstract）
1. **3D 高斯表示**，從 SfM 稀疏點初始化（[[src-colmap]]）。每顆高斯有：
   - 位置（mean）μ
   - 共變異數 Σ（anisotropic），參數化為 `Σ = R S Sᵀ Rᵀ`（旋轉四元數 + 縮放向量），確保永遠是合法的共變異數矩陣
   - 不透明度 α
   - 顏色：[[spherical-harmonics]] 係數（訓練時每 1000 iterations 加一個 band，直到 4 個 band）
   - 見 [[3d-gaussian]]
2. **交錯的最佳化 / 自適應密度控制**（[[adaptive-density-control]]）
   - 每 100 iterations densify 一次，並移除 α 太低的高斯
   - 位置梯度大於閾值（τ_pos = 0.0002）→ 需要密化
   - 重建不足（under-reconstruction）的小高斯 → **Clone**（複製）
   - 過度重建（over-reconstruction）的大高斯 → **Split** 成兩個，尺度除以 φ = 1.6
   - 每 3000 iterations 把 α 重設到接近 0，抑制高斯數量膨脹與 floaters
3. **快速、可感知可見性的 tile-based rasterizer**（[[splatting-rasterization]]）
   - 畫面切成 16×16 tiles，視錐裁切（99% 信賴區間）
   - 用一次 GPU radix sort 依 tile + 深度排序
   - 每個 tile 由前往後 α-blending

## 損失函數
`L = (1 − λ) L1 + λ L_D-SSIM`，λ = 0.2

## 關鍵數字（Table 1，Mip-NeRF360 資料集）
| 方法 | 訓練 | FPS | 記憶體 | PSNR |
|---|---|---|---|---|
| Plenoxels | 25m49s | 6.79 | 2.1GB | 23.08 |
| INGP-Base | 5m37s | 11.7 | 13MB | 25.30 |
| Mip-NeRF360 | 48h | 0.06 | 8.6MB | 27.69 |
| **3DGS-7K** | 6m25s | 160 | 523MB | 25.60 |
| **3DGS-30K** | 41m33s | 134 | 734MB | 27.21 |

> 表中數字已逐列對照 raw/3dgs_2308.04079.txt 第 425–434 行。7K iterations 約 6–8 分鐘就已經很高品質（Fig. 1：51 分鐘達到 SOTA 品質）。
> Mip-NeRF360 不在本 wiki ingest 範圍內，數據僅引用自 3DGS Table 1。

## 限制（Sec. 7.4）
- 沒被拍好的區域有瑕疵
- 可能產生拉長或「斑塊狀（splotchy）」高斯
- 大高斯造成 **popping** artifacts（可見性排序簡化、guard band 剔除）
- 記憶體遠高於 NeRF 類方法：訓練 GPU 記憶體可能超過 20GB；模型數百 MB
- 大場景可能需要調低位置學習率

## 重要觀點
> 與普遍看法相反，**連續表示並非**快速、高品質輻射場訓練的必要條件。

## 相關概念
[[3d-gaussian]] · [[splatting-rasterization]] · [[adaptive-density-control]] · [[volume-rendering]] · [[nerf-vs-3dgs]]
