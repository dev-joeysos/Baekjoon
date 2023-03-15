n = [i+1 for i in range(30)]
for i in range(28):
    t = int(input())
    for j in range(30):
        if t == n[j]:
            n[j] = 0

for i in range(30):
    if n[i] != 0:
        print(n[i])