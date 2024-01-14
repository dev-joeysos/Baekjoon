# 1일 1백준
'''
순열, permutation 문제
N이 3~8로 작기 떄문에 브루트 포스로 해결한다.
순열로 모든 가능한 조합의 리스트를 만든다.
각 조합에 수식을 적용한 값을 구한다.
값의 최대값을 구한다. (최댓값 갱신)
'''
from itertools import permutations

n = int(input())
numbers = list(map(int, input().split()))
per = list(permutations(numbers, n))
answer = 0

for p in per:
    s = 0
    for i in range(n-1):
        s += abs(p[i] - p[i+1])
    answer = max(answer, s)
print(answer)
