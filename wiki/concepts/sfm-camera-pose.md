---
id: sfm-camera-pose
type: concept
sources: [src-colmap, src-nerf, src-3dgs]
---

# 相機位姿與 Structure-from-Motion

**相機位姿（camera pose）**：相機在 3D 空間中的位置與朝向（外參），加上焦距等內參。有了它，才能知道每個像素對應到 3D 空間中的哪一條**光線**。

**為什麼重要**
- NeRF：「the only input required ... is a set of images with known camera poses」（[[src-nerf]] Abstract）
- 3DGS：除了位姿，還用 SfM 的**稀疏點雲**初始化高斯位置（[[src-3dgs]]）

**SfM 怎麼做**：特徵擷取 → 配對 → 幾何驗證 → 初始化 → 逐張註冊 → 三角化 → Bundle Adjustment → 離群點過濾（[[src-colmap]] Fig. 2）

**比喻**：從一疊照片反推「攝影師當時站在哪、鏡頭朝哪」。

**常見失敗**：重複紋理、反光、太少重疊 → 位姿算錯 → 後面的 NeRF/3DGS 全部壞掉（garbage in, garbage out）。
