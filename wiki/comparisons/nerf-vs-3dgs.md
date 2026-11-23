---
id: nerf-vs-3dgs
type: comparison
sources: [src-nerf, src-plenoxels, src-instant-ngp, src-3dgs, src-survey]
---

# NeRF vs 3D Gaussian Splatting

## 概念比較
| 面向 | NeRF | 3DGS |
|---|---|---|
| 場景表示 | MLP（隱式） | 數百萬顆 3D 高斯（顯式） |
| 是否用神經網路 | 是 | **否** |
| 初始化 | 隨機網路權重 | SfM 稀疏點雲 |
| 渲染方式 | Ray marching + 體渲染 | Splatting + tile-based 光柵化 |
| 混合公式 | α-compositing | α-compositing（同一形式） |
| 視角相關顏色 | MLP 輸入方向 d | 球諧函數 |
| 可編輯性 | 難 | 容易 |
| 記憶體 | 小（MB 等級） | 大（數百 MB） |

## 數字比較（[[src-3dgs]] Table 1，Mip-NeRF360 資料集，已核對原文）
| 方法 | 訓練 | FPS | 記憶體 | PSNR↑ |
|---|---|---|---|---|
| NeRF（原版） | 1–2 天（V100，[[src-nerf]]） | ~0.03（30 s/張） | — | — |
| Mip-NeRF360* | 48h | 0.06 | 8.6MB | 27.69 |
| Plenoxels | 25m49s | 6.79 | 2.1GB | 23.08 |
| INGP-Base | 5m37s | 11.7 | 13MB | 25.30 |
| 3DGS-7K | 6m25s | 160 | 523MB | 25.60 |
| 3DGS-30K | 41m33s | 134 | 734MB | 27.21 |

\* Mip-NeRF360 不在本 wiki ingest 範圍，數據引用自 3DGS Table 1，作為「當時品質最好的 NeRF」基準。
原版 NeRF 的列來自 NeRF 論文本身，**不同資料集與硬體，不可直接比較**。

## 一句話總結
NeRF 證明了「可微分體渲染 + 照片」能學出照片級 3D；3DGS 保留同樣的混合公式，但把表示換成顯式高斯、把渲染換成光柵化，換來即時速度與可編輯性，代價是記憶體。
