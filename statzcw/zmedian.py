from typing import List

def zmedian(data: List[float]) -> float :
    data.sort()
    n = len(data)
    if n % 2 == 0:
        median = (data[n//2 - 1] + data[n//2]) / 2
    else:
        median = data[n//2]
    return median