# 수 정렬2
import sys
# 오름차순 정렬
N = int(input())
count = [0]*10001
for i in range(N):
    Num = int(sys.stdin.readline())

    count[Num] += 1

for i in range(10001):
    if count[i] != 0:  # 인덱스가 0이 아닌 경우에만
        for _ in range(count[i]):
            print(i)
