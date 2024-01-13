def solution(box, n):
    volume = 1
    for item in box:
        tmp = item // n
        volume *= tmp
    return volume