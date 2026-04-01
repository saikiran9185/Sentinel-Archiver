# Sentinel-Archiver Performance Benchmarks

## Test Environment
- **Hardware:** MacBook Pro M3 (8GB RAM)
- **Dataset:** 19GB Photography Project (RAW + JPEG)
- **File Count:** ~12,000 files

## Results

| Method | Original Size | Compressed Size | Savings |
| :--- | :--- | :--- | :--- |
| macOS Native ZIP | 19.0 GB | 15.2 GB | **20%** |
| Sentinel V12 (Zlib) | 19.0 GB | 12.7 GB | **33%** |
| Sentinel V16 (LZMA2) | 19.0 GB | 9.5 GB | **50%** |

## Key Observations

- **V16** achieves 50% reduction by using LZMA2 solid blocks on high-redundancy datasets
- **V12** is more stable for mixed file types (3D, documents, photos)
- Format triage (JPEG-XL conversion) adds ~8% additional savings on image-heavy datasets

## Memory Usage (M3 8GB)

| Version | Peak RAM | Notes |
| :--- | :--- | :--- |
| V12 | ~4 GB | Stable under normal workload |
| V14 | ~6 GB | SQLite gating prevents OOM |
| V16 | ~2 GB | Zero-RAM streaming architecture |