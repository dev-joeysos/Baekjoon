N, M = map(int, input().split())
basket = [i+1 for i in range(N)]
for s in range(M):
    i, j = map(int, input().split())
    s = basket[i-1]
    basket[i-1] = basket[j-1]
    basket[j-1] = s
print(*basket)