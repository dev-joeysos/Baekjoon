# 1 일 1 백준
# 2292 번
# 220731

# 최소 벌집 경로

N = int(input())
start = 0
end = 1
i = 0
while True:
    if start <= N <= end:
        print(i+1)
        break
    else:
        i += 1
        start = end + 1
        end = end + (6*i)