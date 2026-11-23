---
id: src-plenoxels
type: source
title: "Plenoxels: Radiance Fields without Neural Networks"
authors: Fridovich-Keil, Yu, Tancik, Chen, Recht, Kanazawa
venue: CVPR 2022
raw: raw/plenoxels_2112.05131.pdf
arxiv: https://arxiv.org/abs/2112.05131
---

# Plenoxels（Fridovich-Keil & Yu et al., 2022）

## 一句話
不用神經網路，直接把顏色和密度存在 3D 格子裡，一樣能做到 NeRF 的品質，而且快 100 倍。

## 核心方法
- **稀疏 voxel grid**：每個被佔用的 voxel 角點存
  - 一個不透明度（opacity）純量
  - 每個顏色通道的 [[spherical-harmonics]] 係數：使用 2 階 SH，每通道 9 個，共 27 個係數 / voxel
- **三線性內插**：任意位置的值由鄰近 voxel 內插得到 → 連續表示。
- **與 NeRF 相同的可微分體渲染**（[[volume-rendering]]）。
- **Coarse-to-fine**：先低解析度（如 256³），剪掉空 voxel，再細分到 512³。
- 正則化：Total Variation（TV）regularizer。

## 關鍵數字
| 項目 | Plenoxels | NeRF | 出處 |
|---|---|---|---|
| 訓練時間（bounded scenes，單張 Titan RTX） | 約 11 分鐘 | 約 1 天 | Sec. 1 |
| 速度提升 | 兩個數量級（>100×） | — | Abstract |
| 渲染 | 約 15 fps（互動等級） | 約 30 秒 / 張 | Sec. 1 |

## 最重要的結論（教學重點）
> "Our experiments suggest the key element of Neural Radiance Fields is not the neural network but the differentiable volumetric renderer."

→ NeRF 成功的關鍵是**可微分體渲染**，而不是神經網路。這打開了「顯式表示也能做輻射場」的路，是走向 [[src-3dgs]] 的重要伏筆。見 [[implicit-vs-explicit]]

## 限制
- 3DGS 論文 Table 1 顯示其記憶體約 2.1–2.7GB、FPS 約 7–13（見 [[nerf-vs-3dgs]]）。
