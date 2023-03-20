N, M = map(int, input().split())
basket = []
for i in range(N):
    basket.append(i+1)  # N = [1, 2, 3, ... N]
for _ in range(M):
    i, j, k = map(int, input().split())
    basket[i-1:j] = basket[k-1:j] + basket[i-1:k-1]

print(*basket)
