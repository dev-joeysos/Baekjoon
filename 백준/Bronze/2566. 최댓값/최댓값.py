# 1 일 1 백준
# 2566 번
# 230728

# 최댓값 탐색 알고리즘
# clone coding

array_9x9 = []
for i in range(9):
    row = list(map(int, input().split()))
    array_9x9.append(row)

max_value = array_9x9[0][0]
max_row = 0
max_col = 0

for i, row in enumerate(array_9x9):
    for j, num in enumerate(row):
        if num > max_value:
            max_value = num
            max_row = i
            max_col = j

print(max_value)
print(max_row + 1, max_col + 1)
