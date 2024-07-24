from typing import List

def zmode(data: List[float]) -> float :
    freq = {}
    max_count = -1
    modes = []

    for num in data:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    for num, count in freq.items():
        if count > max_count:
            max_count = count
            modes = [num]
        elif count == max_count:
            modes.append(num)

    return min(modes)