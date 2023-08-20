'''
특정 조건 이후부터 입력값 넣기
'''
import sys
input = sys.stdin.readline
N = int(input())
S = set()
S.add("ChongChong")
for _ in range(N):
    x, y = input().rstrip().split()
    if x in S:
        S.add(y)

    if y in S:
        S.add(x)

print(len(S))
