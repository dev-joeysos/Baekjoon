T = int(input())
for _ in range(T):
    K, N = map(int, input().split())
    p = 1
    q = 1

    for _ in range(K):
        q *= N
        p *= K
        N -= 1
        K -= 1
    print(q//p)
