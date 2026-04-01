# Sentinel V8.5: Raw Density Specialist
# First implementation of high-redundancy surgical chunking.
import hashlib, zlib, os
CHUNK_SIZE = 64 * 1024
ZLIB_LEVEL = 6
