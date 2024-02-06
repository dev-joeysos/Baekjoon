def solution(n):
    i = 0
    for _ in range(n):
        i += 1
        while i % 3 == 0 or '3' in str(i):
            i += 1
    return i