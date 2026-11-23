---
id: radiance-field
type: concept
sources: [src-nerf, src-plenoxels, src-instant-ngp, src-survey]
---

# 輻射場（Radiance Field）

**定義**：一個函數，告訴你空間中每個點、從每個方向看過去，是什麼**顏色**、有多**「實」**（密度）。
`F(x, y, z, θ, φ) → (RGB, σ)`（[[src-nerf]] Sec. 3）

- **σ（體密度）**：只跟位置有關。可以理解為「光線在這裡被擋住的機率密度」。
- **RGB**：跟位置**和**方向有關 → 能表現反光、高光（non-Lambertian）。

**比喻：一團會回答問題的彩色霧**。你問它「這個點、從這個方向看，是什麼顏色？有多濃？」，它就回答。

**同一個概念，不同的存法**
| 方法 | 怎麼存這個函數 |
|---|---|
| NeRF | 一個 MLP 的權重（[[src-nerf]]） |
| Plenoxels | 稀疏 voxel grid + 球諧函數（[[src-plenoxels]]） |
| Instant-NGP | 多解析度 hash table + 小 MLP（[[src-instant-ngp]]） |
| 3DGS | 數百萬顆 3D 高斯（[[src-3dgs]]） |

→ 見 [[implicit-vs-explicit]]
