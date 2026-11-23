---
id: novel-view-synthesis
type: concept
sources: [src-nerf, src-3dgs, src-survey]
---

# 新視角合成（Novel View Synthesis）

**定義**：給定一個場景的多張照片（及其相機位姿），合成從「沒拍過的角度」看這個場景會長怎樣的照片。

**直覺**：手機繞著一盆花拍 50 張，之後能在螢幕上用任何角度、任何路徑「飛」過這盆花。

**基本流程（本 wiki 的主線）**
```
照片 ──► SfM（COLMAP）求相機位姿 ──► 建立 3D 表示 ──► 從新視角渲染
                                     ├ NeRF：神經網路（隱式）
                                     └ 3DGS：3D 高斯（顯式）
```
- 位姿：[[sfm-camera-pose]]
- 表示：[[radiance-field]]、[[3d-gaussian]]
- 渲染：[[volume-rendering]]、[[splatting-rasterization]]

**歷史脈絡**（[[src-survey]] Sec. 1、[[src-3dgs]] Sec. 2）：light fields（需要密集取樣）→ SfM + multi-view stereo → NeRF（2020）→ 加速（Plenoxels、Instant-NGP，2022）→ 3DGS（2023）。

**應用**：VR/AR、數位分身、機器人導航、文物保存、自駕模擬（[[src-survey]]）。
