N, M = map(int, input().split())
basket = [0]*N
for s in range(M):
    i, j, k = map(int, input().split())
    for t in range(i-1, j):
        basket[t] = k
print(*basket)
