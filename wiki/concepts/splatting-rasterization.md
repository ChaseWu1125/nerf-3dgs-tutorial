---
id: splatting-rasterization
type: concept
sources: [src-3dgs]
---

# Splatting 與 Tile-based 光柵化

**Splatting 是什麼**：把 3D 高斯「拍扁」投影到畫面上，變成一個 2D 的橢圓斑（splat），像把顏料噴到畫布上。

**投影**：3D 共變異數經過相機轉換 W 與投影的 Jacobian J，得到 2D 共變異數
$$\Sigma' = J\,W\,\Sigma\,W^\top J^\top$$
（[[src-3dgs]] Sec. 4，引用 Zwicker et al. 2001）

**為什麼快：反過來做**
| | NeRF（ray marching） | 3DGS（rasterization） |
|---|---|---|
| 方向 | 從每個像素射光線去「找」場景 | 把每個場景元素「投」到畫面 |
| 每像素成本 | 每條光線查詢 MLP 上百次 | 只混合覆蓋到它的 splats |
| GPU 友善度 | 低 | 高（跟遊戲引擎同一套思路） |

**Tile-based rasterizer 步驟**（[[src-3dgs]] Sec. 6）
1. 畫面切成 **16×16 像素的 tiles**
2. 視錐裁切：只保留 99% 信賴區間與視錐相交的高斯
3. 每個高斯依覆蓋的 tile 複製，key = (tile ID, 深度)
4. **一次 GPU radix sort** 完成排序
5. 每個 tile 由前到後做 α-blending，像素累積不透明度飽和就提早停止

**混合公式**：與 NeRF 相同的 α-compositing 形式（[[volume-rendering]]）
$$C=\sum_i \mathbf c_i\,\alpha_i\prod_{j<i}(1-\alpha_j)$$
差別只在 αᵢ 來自 2D 高斯在該像素的值 × 不透明度。

**副作用**：排序以每個高斯為單位而非每像素，可能造成 **popping**（[[src-3dgs]] Sec. 7.4）。
