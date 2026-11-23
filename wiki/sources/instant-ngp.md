---
id: src-instant-ngp
type: source
title: "Instant Neural Graphics Primitives with a Multiresolution Hash Encoding"
authors: Müller, Evans, Schied, Keller (NVIDIA)
venue: SIGGRAPH 2022 (ACM TOG 41(4))
raw: raw/instantngp_2201.05989.pdf
arxiv: https://arxiv.org/abs/2201.05989
---

# Instant-NGP（Müller et al., 2022）

## 一句話
把「記憶」交給一張多解析度的 hash table，神經網路只需要很小，於是 NeRF 可以在幾秒到幾分鐘內訓練完成。

## 核心方法
- **Multiresolution hash encoding**（見 [[hash-encoding]]）
  - 多個解析度層級的格子，每個格點透過 hash 對應到一張表裡**可訓練的特徵向量**。
  - 查詢點在各層級內插特徵 → 串接 → 送進**很小的 MLP**。
  - 不處理 hash collision：多解析度結構讓網路自己分辨（collision 時梯度會被平均，重要的點主導）。
- **Fully-fused CUDA kernels**（tiny-cuda-nn）：減少記憶體頻寬浪費。
- 通用：同一套編碼可用於 gigapixel 影像、SDF、NRC、NeRF。

## 關鍵數字
| 項目 | 數值 | 出處 |
|---|---|---|
| 訓練 | 秒到分鐘等級 | Abstract, Fig. 1 |
| 渲染 | 1920×1080 下數十毫秒 | Abstract |
| 3DGS 論文中的對照（Mip-NeRF360 資料集） | INGP-Base 5m37s、11.7 fps、13MB | 3DGS Table 1 |

## 定位
仍然是**神經網路 + 體渲染**（[[radiance-field]] 的隱式/混合表示），但把大部分容量放到可訓練的資料結構上。
與 [[src-plenoxels]] 同時代，兩者路線不同：Plenoxels 完全拿掉網路，Instant-NGP 保留小網路並加速。

## 限制
- hash collision 會造成一些微小雜訊/表面粗糙（論文 SDF 與 NeRF 結果中可見）。
- 在大場景上品質仍不如 Mip-NeRF360（3DGS Table 1）。
