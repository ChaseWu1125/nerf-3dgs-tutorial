---
id: positional-encoding
type: concept
sources: [src-nerf, src-instant-ngp]
---

# Positional Encoding（位置編碼）

**問題**：直接把 (x, y, z) 丟進 MLP，網路傾向學出**平滑、模糊**的函數，畫不出細節（[[src-nerf]] Sec. 5.1、Fig. 4）。

**做法**：把每個座標 p 映射到一串不同頻率的 sin/cos：
$$\gamma(p)=\big(\sin(2^0\pi p),\cos(2^0\pi p),\dots,\sin(2^{L-1}\pi p),\cos(2^{L-1}\pi p)\big)$$
- 位置 x：L = 10
- 方向 d：L = 4

**比喻**：像給網路一把「有粗刻度也有細刻度的尺」，讓它分得出很靠近的兩個點。

**後續**：Instant-NGP 用**可訓練的** multiresolution hash encoding 取代固定的 sin/cos 編碼（[[hash-encoding]]）。
