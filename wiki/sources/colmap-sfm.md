---
id: src-colmap
type: source
title: "Structure-from-Motion Revisited"
authors: Schönberger, Frahm
venue: CVPR 2016
raw: raw/colmap_sfm_cvpr2016.pdf
code: https://github.com/colmap/colmap
---

# COLMAP / Structure-from-Motion（Schönberger & Frahm, 2016）

## 一句話
從一堆沒有排序的照片，反推出「每張照片是從哪裡、朝哪個方向拍的」，順便得到場景的稀疏 3D 點。

## 為什麼 NeRF/3DGS 需要它
NeRF 與 3DGS 的輸入都是「**照片 + 已知相機位姿**」。真實拍攝時沒有位姿，所以實務上幾乎都先跑 COLMAP。
3DGS 更進一步：直接用 COLMAP 產生的**稀疏點雲當作高斯點的初始位置**（見 [[src-3dgs]]）。

## 增量式 SfM 流程（論文 Fig. 2）
1. **Correspondence search（對應點搜尋）**
   - Feature extraction：在每張圖找局部特徵（如 SIFT）。
   - Matching：找出看到同一場景區域的圖片對。
   - Geometric verification：用幾何模型驗證配對是否真的對。
2. **Incremental reconstruction（增量重建）**
   - Initialization：挑一對好的初始雙視圖（選錯可能永遠救不回來）。
   - Image registration：一張一張把新照片註冊進模型。
   - Triangulation：三角化出 3D 點。
   - Bundle Adjustment（BA）：同時微調所有相機與 3D 點，最小化重投影誤差。
   - Outlier filtering：剔除錯誤點。

## 產出
- 每張照片的相機內參與外參（位姿）
- **稀疏點雲**（sparse point cloud）

## 教學比喻
從一疊照片反推「攝影師當時站在哪、鏡頭朝哪」。

## 相關概念
[[sfm-camera-pose]] · [[novel-view-synthesis]]
