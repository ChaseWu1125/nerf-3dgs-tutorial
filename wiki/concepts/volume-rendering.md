---
id: volume-rendering
type: concept
sources: [src-nerf, src-plenoxels, src-3dgs]
---

# 體渲染（Volume Rendering）

**問題**：有了一團彩色的霧（[[radiance-field]]），一個像素應該是什麼顏色？

**直覺**：從相機穿過像素射出一條光線。沿路上每一小段霧都會「貢獻一點顏色」，但前面的霧越濃，後面的霧就越難被看到。

## 連續形式（[[src-nerf]] Eq. 1）
$$C(\mathbf r)=\int_{t_n}^{t_f} T(t)\,\sigma(\mathbf r(t))\,\mathbf c(\mathbf r(t),\mathbf d)\,dt,\qquad T(t)=\exp\!\Big(-\int_{t_n}^{t}\sigma(\mathbf r(s))\,ds\Big)$$

## 離散形式（[[src-nerf]] Eq. 3；[[src-plenoxels]] Eq. 1 相同）
$$\hat C(\mathbf r)=\sum_{i=1}^{N} T_i\,\big(1-e^{-\sigma_i\delta_i}\big)\,\mathbf c_i,\qquad T_i=\exp\!\Big(-\sum_{j=1}^{i-1}\sigma_j\delta_j\Big)$$

| 符號 | 意義 | 白話 |
|---|---|---|
| σᵢ | 第 i 個樣本的密度 | 這裡的霧多濃 |
| δᵢ | 到下一個樣本的距離 | 這一小段有多長 |
| 1 − e^(−σᵢδᵢ) = αᵢ | 這一段的不透明度 | 這段「吸收/發出」多少光 |
| Tᵢ | 累積穿透率 | 光有多少比例**還沒被前面擋掉** |
| cᵢ | 顏色 | 這段霧的顏色 |

令 αᵢ = 1 − exp(−σᵢδᵢ)，就變成傳統的 **alpha compositing**（[[src-nerf]] Sec. 4）：
$$\hat C=\sum_i \mathbf c_i\,\alpha_i\prod_{j<i}(1-\alpha_j)$$

## 為什麼這條公式是全部的核心
1. **可微分** → 渲染誤差可以反傳回場景參數，用梯度下降學出場景（[[src-nerf]]）。
2. Plenoxels 證明：關鍵是這個可微分渲染器，不是神經網路（[[src-plenoxels]]）。
3. **3DGS 用的是同一種 α-blending 形式**，只是 αᵢ 來自投影到畫面上的 2D 高斯，而不是沿光線取樣的密度（[[src-3dgs]] Sec. 4、[[splatting-rasterization]]）。

## 為什麼 NeRF 慢
每個像素沿光線取 64 + 128 個點、每點都要跑一次 MLP（[[src-nerf]] Sec. 5.2）。
