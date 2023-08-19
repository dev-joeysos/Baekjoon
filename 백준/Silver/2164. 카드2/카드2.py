import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
Q = deque(range(1, N+1))

while len(Q) > 1:
    Q.popleft()  # 첫 번째 숫자 제거
    Q.append(Q.popleft())  # 두 번째 숫자를 빼서 덱의 끝에 추가

print(Q[0])
