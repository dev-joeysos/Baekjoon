# 블랙잭
N, M = map(int, input().split())
value = list(map(int, input().split()))

result = 0

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            sum = value[k] + value[j]+value[i]
            if sum <= M:  # 세 카드의 합이 조건 수보다 작은 경우만
                result = max(result, sum)

print(result)
