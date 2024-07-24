from typing import List
from statzcw.zstddev import zstddev
from statzcw.zmean import zmean


def cov(data_x: List[float], data_y: List[float]):
    mean_x = zmean(data_x)
    mean_y = zmean(data_y)
    sum_cov = sum((x - mean_x) * (y - mean_y) for x, y in zip(data_x, data_y))
    return sum_cov / (len(data_x) - 1)


def zcorr(data1: List[float], data2: List[float]) -> float :
    corr = cov(data1, data2) / (zstddev(data1) * zstddev(data2))
    return corr