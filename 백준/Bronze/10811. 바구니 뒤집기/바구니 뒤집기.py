N, M = map(int, input().split())
n = [i+1 for i in range(N)]
for i in range(M):
    i, j = map(int, input().split())
    # 역순정렬 함수 reversed()
    n[i-1:j] = reversed(n[i-1:j])
print(*n)