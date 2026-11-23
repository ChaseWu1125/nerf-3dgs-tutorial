---
id: src-survey
type: source
title: "A Survey on 3D Gaussian Splatting"
authors: Guikun Chen, Wenguan Wang (Zhejiang University)
venue: arXiv 2401.03890 (v9, Apr 2026)
raw: raw/survey3dgs_2401.03890.pdf
---

# A Survey on 3D Gaussian Splatting（Chen & Wang）

## 一句話
3DGS 的第一篇系統性綜述：原理、改進方向、應用領域、效能比較與未來挑戰。

## 核心定位
- 主流 NeRF 是**隱式**神經模型；3DGS 用**數百萬個可學習的 3D 高斯**做**顯式**場景表示。
- 搭配可微分渲染 → **即時渲染**與**前所未有的可編輯性**。見 [[implicit-vs-explicit]]

## 方法改進方向（Sec. 4）
記憶體效率（壓縮）、照片真實度、最佳化演算法、混合表示、新渲染演算法、kernel 設計（非高斯基元）等。

## 應用領域（Sec. 5）
| 領域 | 例子 |
|---|---|
| Robotics | SLAM、操作與導航 |
| 動態場景 | 4D / 隨時間變化的場景 |
| 生成與編輯 | text-to-3D、場景編輯 |
| Avatar | 數位人 |
| 內視鏡 | 手術場景重建 |
| 大規模場景 | 城市、街景 |
| Physics | 物理模擬 |

## 未來方向（Sec. 7）
- 具備物理與語意的場景表示（Physics- and Semantics-aware）
- 從大規模資料學物理先驗
- 3D world modeling
- 前饋式（feed-forward）直接預測高斯，不用逐場景最佳化
- 用 3DGS 建模物體內部結構
- 自駕等模擬

## 相關
[[src-3dgs]] · [[nerf-vs-3dgs]]
