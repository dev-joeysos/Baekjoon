X = int(input())
N = int(input())  # 구매한 목록의 종류 (줄)
result = [0 for i in range(N)]
for i in range(N):
    a, b = map(int, input().split())
    result[i] = a*b

total = sum(result)
if total == X:
    print("Yes")
else:
    print("No")