---
id: misconceptions
type: checklist
purpose: 供「檢查節點」逐條比對簡報內容
---

# 常見誤解清單（Fact-check Checklist）

每條都附「正確說法」與 wiki 出處。生成的簡報必須逐條通過。

| # | 誤解 | 正確說法 | 出處 |
|---|---|---|---|
| M1 | 3DGS 是一種神經網路 / 用 MLP | 3DGS **沒有神經網路**，參數直接最佳化 | [[src-3dgs]]、[[3d-gaussian]] |
| M2 | NeRF 輸出一個 mesh | NeRF 輸出隱式輻射場（顏色+密度），要另外萃取才有 mesh | [[src-nerf]]、[[radiance-field]] |
| M3 | 3DGS 從隨機點開始 | 3DGS 從 **SfM 稀疏點雲**初始化 | [[src-3dgs]]、[[sfm-camera-pose]] |
| M4 | NeRF 的密度也隨視角改變 | σ **只依賴位置**；只有顏色依賴方向 | [[src-nerf]] Sec. 3 |
| M5 | NeRF/3DGS 不需要相機位姿 | 兩者都需要已知位姿（通常由 COLMAP 算） | [[src-colmap]] |
| M6 | NeRF 用 CNN | NeRF 用全連接 MLP（無卷積層） | [[src-nerf]] |
| M7 | 3DGS 全面優於 NeRF | 3DGS 記憶體大很多；Mip-NeRF360 PSNR 仍略高 | [[nerf-vs-3dgs]] |
| M8 | Plenoxels 證明神經網路是關鍵 | 相反：關鍵是**可微分體渲染器** | [[src-plenoxels]] |
| M9 | 3DGS 的高斯是球形 | 是 **anisotropic**（可拉長旋轉）橢圓 | [[3d-gaussian]] |
| M10 | 跨論文的時間/FPS 數字可直接比 | 不同資料集與 GPU，要註明出處 | [[nerf-vs-3dgs]] |

## 數字核對規則
- 所有數字必須能在 `raw/*.txt` 找到原文（grep 驗證）
- 投影片上的每個數字要標註來源論文
