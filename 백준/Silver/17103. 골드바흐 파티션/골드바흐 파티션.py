import math
import sys

MAX_N = 1000000  # 예시로 1,000,000을 최대값으로 설정. 문제의 제한에 따라 변경 가능

def is_prime(N):
    arr = [True for _ in range(N+1)]
    arr[0], arr[1] = False, False
    for i in range(2, int(math.sqrt(N)+1)):
        if arr[i]:
            for j in range(i*i, N+1, i):
                arr[j] = False
    return arr

prime_list = is_prime(MAX_N)

T = int(input())
for _ in range(T):
    N = int(sys.stdin.readline())
    count = 0

    for num in range(2, N//2 + 1):
        if prime_list[num] and prime_list[N - num]:
            count += 1

    print(count)
