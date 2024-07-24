from typing import List
from math import sqrt
from statzcw.zstddev import zstddev

def zstderr(data: List[float]) -> float :
    std_err = zstddev(data) / sqrt((len(data)))
    return std_err