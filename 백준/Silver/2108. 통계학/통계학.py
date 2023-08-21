'''
통계
'''
from collections import Counter
import sys
input = sys.stdin.readline
N = int(input())  # 홀수
arr = []
for _ in range(N):
    x = int(input())
    arr.append(x)

a = sum(arr)/N
print(round(a))
arr.sort()
median = (N-1)//2
print(arr[median])

cnt = Counter(arr)  # 내림차순으로 빈도 수 검사
most_commons = cnt.most_common()
max_val = most_commons[0][1]

modes = []
for num, freq in cnt.items():
    if freq == max_val:
        modes.append(num)

if len(modes) > 1:
    print(sorted(modes)[1])
else:  # 1
    print(modes[0])

print(max(arr)-min(arr))
