# greedy
n = int(input())
ropes = []
results = []
for _ in range(n):
    rope = int(input())
    ropes.append(rope)

ropes.sort(reverse=True)

for i in range(n):
    results.append((i+1)*ropes[i])

print(max(results))