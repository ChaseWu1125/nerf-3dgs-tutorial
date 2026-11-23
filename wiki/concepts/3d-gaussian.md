---
id: 3d-gaussian
type: concept
sources: [src-3dgs, src-survey]
---

# 3D 高斯（3D Gaussian 基元）

**比喻：幾百萬顆彩色、半透明、可以拉長旋轉的噴漆點**。每顆都是一個模糊的橢圓球，疊在一起就形成整個場景。

**每顆高斯的參數**（[[src-3dgs]] Sec. 4）
| 參數 | 意義 |
|---|---|
| 位置 μ（mean） | 在哪裡 |
| 共變異數 Σ | 形狀：多大、往哪個方向拉長（anisotropic，非球形） |
| 不透明度 α | 多透明 |
| SH 係數 | 顏色，且隨視角改變（[[spherical-harmonics]]） |

**共變異數怎麼參數化**：直接用梯度下降更新 Σ 可能變成不合法（非半正定）的矩陣，所以拆成
$$\Sigma = R\,S\,S^\top R^\top$$
R 由四元數（rotation）得到、S 由縮放向量（scale）得到 → 永遠合法。

**初始化**：從 SfM 稀疏點雲開始（[[sfm-camera-pose]]），初始為等向性（isotropic）高斯。

**為什麼要 anisotropic**：細長結構（樹枝、電線）可以用少量拉長的高斯表示，比球形省很多（[[src-3dgs]] ablation：Isotropic 品質明顯變差）。

**數量**：場景通常有**數百萬顆**高斯（[[src-survey]] Abstract），模型數百 MB（[[nerf-vs-3dgs]]）。

**3DGS 沒有神經網路**：所有參數都是直接最佳化的顯式數值（[[implicit-vs-explicit]]）。
