# 1일 1백준
N, L = map(int, input().split())
hole = sorted(list(map(int, input().split())))

start = hole[0]
count = 1

for h in hole[1:]:
    if h in range(start, start + L):
        continue
    else:
        start = h
        count += 1
print(count)