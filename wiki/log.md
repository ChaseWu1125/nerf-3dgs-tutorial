# Wiki Log（append-only）

## 2026-11-23 · 主題討論
- 候選主題：RAG（AI 建議）、MCP、Prompt Engineering、學習科學
- **決定：NeRF / 3DGS**（使用者自己的研究主題）
- 理由：使用者具備專業，可擔任「專家審查」節點；有清楚的演進故事線；視覺化素材豐富

## 2026-11-23 · Ingest 前討論（先討論、後生成）
AI 下載 6 篇論文 → 轉文字 → 讀 abstract / intro / method / limitation → 向使用者提出各篇重點與 4 個待決問題：

| 問題 | 使用者決定 |
|---|---|
| Q1 體渲染公式要不要放進簡報 | **要放**，使用者認為很重要 |
| Q2 Mip-NeRF360（未 ingest）如何處理 | 只出現在比較表，標註引用自 3DGS Table 1 |
| Q3 教學比喻（攝影師站位 / 彩色霧 / 噴漆點） | 同意 |
| Q4 常見誤解清單 | 照 AI 提案 → 寫成 [misconceptions.md](misconceptions.md) |

## 2026-11-23 · Ingest
| 順序 | Source | 產生 / 更新頁面 |
|---|---|---|
| 1 | NeRF | sources/nerf, radiance-field, volume-rendering, positional-encoding |
| 2 | COLMAP | sources/colmap-sfm, sfm-camera-pose |
| 3 | Plenoxels | sources/plenoxels, spherical-harmonics, volume-rendering（補充 Eq.1 相同）, implicit-vs-explicit |
| 4 | Instant-NGP | sources/instant-ngp, hash-encoding |
| 5 | 3DGS | sources/3dgs, 3d-gaussian, splatting-rasterization, adaptive-density-control, nerf-vs-3dgs |
| 6 | Survey | sources/survey-3dgs, novel-view-synthesis（應用）, implicit-vs-explicit（可編輯性） |

## 2026-11-23 · Wiki 事實檢查（check node #1）
方法：對 wiki 中每個數字與關鍵論述，`grep raw/*.txt` 找到原文行號。

| 檢查項 | 結果 | 原文位置 |
|---|---|---|
| 3DGS-30K 一列（41m33s / 134 fps / 734MB / 27.21）| ⚠ 初稿**憑記憶填寫、未附出處** → 回頭 grep 驗證 → 正確，補上行號註記 | 3dgs.txt L434 |
| 3DGS Table 1 其他列 | ✅ | L425–432 |
| NeRF L=10 / L=4、Nc=64 / Nf=128、1–2 天、30 s/張 | ✅ | nerf.txt L343, L425, L431, L870 |
| Plenoxels 11 分鐘 / Titan RTX / 15 fps / 27 SH 係數 | ✅ | plenoxels.txt L45–46 |
| 3DGS λ=0.2、τ_pos=0.0002、φ=1.6、每 100 / 3000 iter | ✅ | 3dgs.txt L293–346 |
| 3DGS 16×16 tiles、99% 信賴區間、radix sort | ✅ | L394–397, L853 |
| 3DGS SH 每 1000 iter 加一 band 至 4 bands | ✅ | L443–444 |
| 初始 isotropic、clone 沿位置梯度移動 | ✅ | L323, L327 |
| 「continuous representation is not strictly necessary」 | ✅ | L625–626 |
| 章節編號（NeRF Sec.4/5.x、3DGS Sec.4/5/6/7.4） | ✅ | 各章標題行 |
| 3DGS SH 48 係數 | ⚠ 原文未直接寫，屬**推導** → 在頁面上標註「由 4 bands 推得」 | — |

**學到的事**：最容易出錯的是「AI 自己很有把握的數字」。之後規則：**寫入 wiki 前，每個數字都要先有行號**（把檢查從 wiki 寫完後提前到寫入當下）。

## 2026-11-23 · 查詢 Wiki → 生成簡報
- 大綱 19 頁、6 段；每頁頁尾標「Wiki：頁面 ｜ 來源：論文章節」
- 依 Q1 決定，新增進階公式頁（vr-formula，對應 concepts/volume-rendering.md）
- 依 Q2 決定，Mip-NeRF360 只出現在 compare 頁並加註
- 小測驗 5 題取自 misconceptions.md（M1、M4、M3、M5、M7）

## 2026-11-23 · 簡報檢查（check node #2）
| 檢查 | 結果 |
|---|---|
| tools/check_deck.py：出處標註、Wiki 連結存在、數字 ⊂ Wiki | ✅ 19/19 |
| 誤解清單 M1–M10 人工比對 | ✅ 無違反 |
| 版面高度估算（可用 ≤ 920px） | ⚠ gs-idea ≈ 968px、vr-intuition ≈ 905px → 縮小 padding/gap，重新發布 v7 |
| 視覺預覽（headless Chrome） | ⚠ 本機沒有產生截圖 → 改用規格估算 |

**workflow 修改**：版面預算從「生成後檢查」提前到「擬大綱」階段。
