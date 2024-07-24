from typing import List
from statzcw.zmean import zmean

def zvariance(data: List[float]) -> float :
    n = len(data) - 1
    deviations = [(x - zmean(data)) ** 2 for x in data]

    variance = sum(deviations) / n
    return variance