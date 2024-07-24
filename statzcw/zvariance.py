from typing import List
from statzcw.zmean import zmean

def zvariance(data: List[float]) -> float :
    n = len(data) - 1
    deviations = []
    for x in data:
        deviations.append(abs(zmean(data)-x) ** 2) #abs not allow??

    variance = sum(deviations) / n
    return variance