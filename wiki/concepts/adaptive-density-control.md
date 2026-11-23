---
id: adaptive-density-control
type: concept
sources: [src-3dgs]
---

# 自適應密度控制（Adaptive Density Control）

**問題**：SfM 點雲很稀疏，有些地方高斯太少（細節不夠），有些地方一顆大高斯蓋住太多細節。

**解法**（[[src-3dgs]] Sec. 5.2，Fig. 4）
- 每 **100 iterations** 檢查一次（warm-up 之後）
- 觀察**視空間位置梯度**：平均梯度 > τ_pos = **0.0002** → 這裡需要更多高斯

| 情況 | 判斷 | 動作 |
|---|---|---|
| Under-reconstruction（缺幾何） | 高斯小 | **Clone**：複製一份，沿梯度方向移動 |
| Over-reconstruction（一顆蓋太大） | 高斯大 | **Split**：換成 2 顆，尺度 ÷ φ=**1.6** |
| 幾乎透明 | α < ε_α | **Prune**：刪除 |
| 抑制 floaters 與數量膨脹 | 每 **3000** iterations | 把 α 重設到接近 0 |

**比喻**：畫家先隨手點幾個色點，哪裡細節不夠就多點幾下（clone）、哪個色塊太粗就拆成小色點（split）、沒用的顏料擦掉（prune）。

**損失**：`L = 0.8·L1 + 0.2·L_D-SSIM`（λ=0.2）
