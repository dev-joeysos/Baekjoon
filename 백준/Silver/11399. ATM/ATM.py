import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
rst = 0
# 누적합 구하기
for i in range(len(arr)):  # 5
    for j in range(0, i+1):
        rst += arr[j]
print(rst)
