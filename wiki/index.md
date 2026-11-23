# LLM Wiki：從照片到 3D 世界 —— NeRF 與 3D Gaussian Splatting

> 主題簡介：本 Wiki 整理「新視角合成」從 NeRF（2020）到 3D Gaussian Splatting（2023）的核心概念與演進。
> 知識全部來自 6 篇 ingest 的論文（`raw/`），每個概念頁都標注來源，供教學簡報生成與事實檢查使用。

## 閱讀主線
1. [[novel-view-synthesis]] —— 我們要解決什麼問題
2. [[sfm-camera-pose]] —— 第 0 步：相機位姿
3. [[radiance-field]] → [[volume-rendering]] → [[positional-encoding]] —— NeRF 的三個核心
4. [[hash-encoding]]、[[spherical-harmonics]] —— 加速之路
5. [[3d-gaussian]] → [[splatting-rasterization]] → [[adaptive-density-control]] —— 3DGS 的三個核心
6. [[implicit-vs-explicit]]、[[nerf-vs-3dgs]] —— 統整比較
7. [[misconceptions]] —— 常見誤解與事實檢查清單

## Sources（6 篇）
| id | 論文 | 年份 | 頁面 |
|---|---|---|---|
| src-colmap | Structure-from-Motion Revisited（COLMAP） | CVPR 2016 | [sources/colmap-sfm.md](sources/colmap-sfm.md) |
| src-nerf | NeRF | ECCV 2020 | [sources/nerf.md](sources/nerf.md) |
| src-plenoxels | Plenoxels | CVPR 2022 | [sources/plenoxels.md](sources/plenoxels.md) |
| src-instant-ngp | Instant-NGP | SIGGRAPH 2022 | [sources/instant-ngp.md](sources/instant-ngp.md) |
| src-3dgs | 3D Gaussian Splatting | SIGGRAPH 2023 | [sources/3dgs.md](sources/3dgs.md) |
| src-survey | A Survey on 3D Gaussian Splatting | arXiv 2024–2026 | [sources/survey-3dgs.md](sources/survey-3dgs.md) |

## Concepts（11 頁）
| 頁面 | 一句話 | 主要來源 |
|---|---|---|
| [novel-view-synthesis](concepts/novel-view-synthesis.md) | 從照片合成沒拍過的視角 | nerf, 3dgs, survey |
| [sfm-camera-pose](concepts/sfm-camera-pose.md) | 反推攝影師站位 | colmap |
| [radiance-field](concepts/radiance-field.md) | 會回答問題的彩色霧 | nerf |
| [volume-rendering](concepts/volume-rendering.md) | 沿光線累積顏色的可微分公式 | nerf, plenoxels, 3dgs |
| [positional-encoding](concepts/positional-encoding.md) | 讓 MLP 畫得出細節 | nerf |
| [hash-encoding](concepts/hash-encoding.md) | 可訓練的多層索引表 | instant-ngp |
| [spherical-harmonics](concepts/spherical-harmonics.md) | 不用網路表示視角相關顏色 | plenoxels, 3dgs |
| [3d-gaussian](concepts/3d-gaussian.md) | 彩色半透明可拉伸的噴漆點 | 3dgs |
| [splatting-rasterization](concepts/splatting-rasterization.md) | 把高斯拍扁投到畫面 | 3dgs |
| [adaptive-density-control](concepts/adaptive-density-control.md) | clone / split / prune | 3dgs |
| [implicit-vs-explicit](concepts/implicit-vs-explicit.md) | 存在網路裡 vs 存在資料結構裡 | all |

## Comparisons & Checklists
- [comparisons/nerf-vs-3dgs.md](comparisons/nerf-vs-3dgs.md)
- [misconceptions.md](misconceptions.md)

## 維護紀錄
見 [log.md](log.md)
