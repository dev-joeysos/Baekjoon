# 좌표 정렬2
import sys
N = int(input())
result = []
for _ in range(N):
    x = sys.stdin.readline().strip()
    result.append(x)
result = list(set(result))  # 중복 제거
result.sort()  # 사전순
result.sort(key=lambda x: len(x))  # 길이 순으로 한 번 더
for val in result:
    print(val)
