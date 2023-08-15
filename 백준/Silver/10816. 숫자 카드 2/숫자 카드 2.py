N = int(input())
N_lst = list(map(int, input().split()))
M = int(input())
M_lst = list(map(int, input().split()))

dict = {}
for num in M_lst:
    dict[num] = 0

count = []
for num in N_lst:
    if num in dict:
        dict[num] += 1

for num in M_lst:
    count.append(dict[num])

print(' '.join(map(str, count)))