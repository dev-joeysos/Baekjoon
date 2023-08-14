# sort inside
# 내림차순 정렬

N = int(input())
result = []
while True:
    if N == 0:
        break
    remain = N % 10
    result.append(str(remain))
    N = N//10

result.sort()
result.reverse()

print(''.join(result))
