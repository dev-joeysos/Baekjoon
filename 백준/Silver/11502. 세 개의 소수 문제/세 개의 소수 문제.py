# 1일 1백준
import math

def solution(N):
    array = [True for i in range(N+1)]

    for i in range(2, int(math.sqrt(N)) + 1):
        if array[i] == True:
            j = 2
            while i*j<=N:
                array[i*j] = False
                j += 1

    result = []
    for i in range(2, N+1):
        if array[i] == True:
            result.append(i)
    return result

n = int(input())
for _ in range(n):
    N = int(input())
    lst = solution(N)
    answer = []
    for a in lst:
        for b in lst:
            for c in lst:
                if a + b + c == N:
                    answer.append([a, b, c])
    answer = sorted(answer, key=lambda x: (x[0], x[1], x[2]))

    if len(answer) == 0:
        print(0)
    else:
        print(*answer[0])