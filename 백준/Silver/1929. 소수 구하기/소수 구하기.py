import math
M, N = map(int, input().split())


def is_prime(N):
    arr = [True for _ in range(N+1)]
    arr[0], arr[1] = False, False
    for i in range(2, int(math.sqrt(N)+1)):
        if arr[i] == True:  # 아직 소수면
            j = 2
            while i*j <= N:
                arr[i*j] = False
                j += 1
    return arr


N_lst = is_prime(N)

for i in range(M, N+1):
    if N_lst[i]:
        print(i)