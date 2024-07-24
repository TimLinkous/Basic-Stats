from typing import List
from statzcw.zmean import zmean

def zvariance(data: List[float]) -> float :
    mean = zmean(data)
    deviations = [(x - mean) ** 2 for x in data]
    variance = sum(deviations) / (len(data) - 1)
    return variance