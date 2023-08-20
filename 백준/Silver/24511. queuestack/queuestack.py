'''
덱 (deque)
'''
from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
qs = list(map(int, input().split()))  # [0 1 1 0]
d = list(map(int, input().split()))  # [1 2 3 4]
M = int(input())
m = list(map(int, input().split()))  # [2 4 7]

new_d = deque()
result = []

for i in range(N):
    if qs[i] == 0:
        new_d.append(d[i])  # [1 4]

for num in m:
    if len(new_d) == 0:  # all stack
        result.append(num)
    else:
        X = new_d.pop()
        new_d.appendleft(num)
        result.append(X)
print(' '.join(map(str, result)))