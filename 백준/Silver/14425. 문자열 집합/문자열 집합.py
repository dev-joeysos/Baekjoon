N, M = map(int, input().split())
S = []
Q = []
for _ in range(N):
    x = input()
    S.append(x)

for _ in range(M):
    x = input()
    Q.append(x)

dict = {}
for word in S:
    dict[word] = 1  # 애매

count = 0
for letter in Q:
    if letter in dict:
        count += 1

print(count)