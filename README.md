# Sentinel-Archiver (V8.5 - V17)
### Advanced Cold-Storage Compression for macOS (M3 8GB RAM Optimized)

This repository tracks the evolution of a custom deduplicating compression engine built to outperform Apple Native ZIP by 20-50% on massive 3D and Photography datasets.

## 📈 The Evolution Path
- **V12 [Stable Hybrid]:** The most reliable production version for general tasks. Uses Zlib pre-compression.
- **V16 [Solid Sentinel]:** High-density experiment using LZMA2 Solid blocks. (Known to hit memory limits on 8GB RAM at 300k+ files).
- **V17 [Ghost Engine]:** The Final Form. Implements **Zero-RAM Architecture**. Processes 1TB+ datasets by streaming metadata directly to SQLite, bypassing Python's memory bottlenecks.

## 🚀 Key Features
- **Format Triage:** Automated lossless conversion of PNG/JPG to JPEG-XL before archival.
- **Global Deduplication:** 128KB block-level hashing to eliminate redundant data across file boundaries.
- **8GB RAM Shield:** Architected specifically to handle large swap files and BufferedWriter protection on M3 Silicon.
