---
id: hash-encoding
type: concept
sources: [src-instant-ngp]
---

# Multiresolution Hash Encoding

**想法**：與其讓大 MLP 記住整個場景，不如把「記憶」放進一張可訓練的表，MLP 只要很小。

**步驟**（[[src-instant-ngp]] Sec. 3）
1. 準備 L 個解析度層級的網格（從粗到細）。
2. 對查詢點，在每一層找到周圍的格點，用 hash 函數把格點對應到該層 hash table 中的**可訓練特徵向量**。
3. 內插得到每一層的特徵，串接起來。
4. 送進很小的 MLP 輸出結果（如 σ、RGB）。

**Hash collision 怎麼辦？** 不處理。多個點撞到同一格時梯度會被平均；真正重要（可見、表面附近）的點梯度較大而主導，而不同解析度的層級讓網路能分辨。

**比喻**：像圖書館的多層索引卡：粗層告訴你在哪一區，細層告訴你在哪一格；偶爾兩本書共用一張卡，但查好幾層就分得出來。

**效果**：NeRF 訓練從「天」縮到「秒～分鐘」（搭配 fully-fused CUDA）。
