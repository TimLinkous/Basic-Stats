from typing import List
from math import sqrt
from statzcw.zvariance import zvariance

def zstddev(data: List[float]) -> float :
    std_dev = sqrt(zvariance(data))
    return std_dev
    