import math
import sys

MAX_N = 1000000


def is_prime(N):
    arr = [True for _ in range(N+1)]
    arr[0], arr[1] = False, False
    for i in range(2, int(math.sqrt(N)+1)):
        if arr[i] == True:
            j = 2
            while i*j <= N:
                arr[i*j] = False
                j += 1
    return arr


# 미리 제한 범위의 소수 리스트를 만든다
# N을 2로 나눈 소수까지만 합의 여부를 확인하면 된다
# 해당 합 조건을 만족하는 소수가 존재하면 count +1
T = int(input())
prime_list = is_prime(MAX_N)
for _ in range(T):
    N = int(sys.stdin.readline())
    count = 0
    for num in range(2, N//2 + 1):
        if prime_list[num] and prime_list[N - num]:
            count += 1
    print(count)