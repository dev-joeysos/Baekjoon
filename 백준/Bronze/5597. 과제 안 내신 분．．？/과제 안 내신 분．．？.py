n = [i+1 for i in range(30)]
for i in range(28):
    t = int(input())
    n[n.index(t)] = 0

print(*[i for i in n if i != 0])