# 1 일 1 백준
# 10798 번
# 230728

# 이차원 리스트 세로로 읽기(반전)

array_15x5 = [["*" for _ in range(15)] for _ in range(5)]
for i in range(5):
    row = list(input())
    for j in range(len(row)):
        array_15x5[i][j] = row[j]

for i in range(15):
    for j in range(5):
        if array_15x5[j][i] != "*":
            print(array_15x5[j][i], end='')
