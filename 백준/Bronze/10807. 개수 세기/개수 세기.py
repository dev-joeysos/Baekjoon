N = int(input())
li = list(map(int, input().split()))
v = int(input())

count = 0
for i in range(N):
    if v == li[i]:
        count += 1
print(count)