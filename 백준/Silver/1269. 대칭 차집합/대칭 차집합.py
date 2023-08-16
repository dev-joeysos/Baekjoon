A, B = map(int, input().split())
A_set = set(map(int, input().split()))
B_set = set(map(int, input().split()))

PA = []
PB = []
for num in A_set:
    if num not in B_set:
        PA.append(num)

for num in B_set:
    if num not in A_set:
        PB.append(num)

print(len(PA) + len(PB))
