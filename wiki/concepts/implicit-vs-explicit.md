---
id: implicit-vs-explicit
type: concept
sources: [src-nerf, src-plenoxels, src-instant-ngp, src-3dgs, src-survey]
---

# 隱式表示 vs 顯式表示

| | 隱式（Implicit） | 顯式（Explicit） |
|---|---|---|
| 場景存在哪 | 神經網路權重裡 | 直接可讀的資料結構（voxel、點、高斯） |
| 要知道某點的顏色 | 問網路（跑一次 forward） | 直接查/內插 |
| 代表 | NeRF | Plenoxels（voxel）、3DGS（高斯） |
| 優點 | 儲存小、連續 | 快、**可編輯**（可直接移動/刪除元素） |
| 缺點 | 慢、難編輯 | 記憶體大 |

**混合**：Instant-NGP = 顯式的 hash table 特徵 + 小 MLP。

**演進故事（本 wiki 的教學主線）**
1. NeRF（2020）：隱式 MLP，品質好但慢 —— [[src-nerf]]
2. Plenoxels（2022）：拿掉網路，證明關鍵是可微分體渲染 —— [[src-plenoxels]]
3. Instant-NGP（2022）：資料結構扛大部分工作，小網路 —— [[src-instant-ngp]]
4. 3DGS（2023）：顯式高斯 + 光柵化 → 即時；「連續表示並非必要」—— [[src-3dgs]]
5. Survey：3DGS 的顯式性帶來前所未有的可編輯性 —— [[src-survey]]
