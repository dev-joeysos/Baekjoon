import math


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


while True:
    n = int(input())
    if n == 0:
        break

    count = 0
    k = 2*n
    n_lst = is_prime(k)
    for i in range(n+1, k+1):
        if n_lst[i]:
            count += 1
    print(count)