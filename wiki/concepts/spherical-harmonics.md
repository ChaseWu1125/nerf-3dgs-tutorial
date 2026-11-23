---
id: spherical-harmonics
type: concept
sources: [src-plenoxels, src-3dgs]
---

# 球諧函數（Spherical Harmonics, SH）

**用途**：表示「顏色隨觀看方向改變」這件事，而不需要神經網路。

**直覺**：SH 是球面上的一組基底函數（像傅立葉級數，但在球面上）。
- 低階（band 0）：各方向都一樣的顏色（像霧面、Lambertian）
- 高階：方向變化快的效果（像高光、反光）

顏色 = Σ（係數 × 基底函數在該方向的值），係數是要學的參數。

**用法比較**
| 方法 | SH 階數 | 每通道係數 | 出處 |
|---|---|---|---|
| Plenoxels | degree 2 | 9（共 27 / voxel） | [[src-plenoxels]] Sec. 3.2 |
| 3DGS | 最終 4 個 band（degree 3） | 16（共 48 / 高斯） | [[src-3dgs]]：每 1000 iterations 加一個 band，直到 4 個 band |

> 3DGS 的 48 係數由「4 bands → 16 個基底 × 3 色」推得。
