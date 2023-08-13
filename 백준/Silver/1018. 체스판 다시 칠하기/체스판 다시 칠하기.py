N, M = map(int, input().split())
data = [input() for _ in range(N)]


def count_color(x, y):
    start_W = ['WBWBWBWB', 'BWBWBWBWBW', 'WBWBWBWB', 'BWBWBWBWBW',
               'WBWBWBWB', 'BWBWBWBWBW', 'WBWBWBWB', 'BWBWBWBWBW']
    start_B = ['BWBWBWBW', 'WBWBWBWBWB', 'BWBWBWBW', 'WBWBWBWBWB',
               'BWBWBWBW', 'WBWBWBWBWB', 'BWBWBWBW', 'WBWBWBWBWB']

    count_W = 0
    count_B = 0
    for i in range(8):
        for j in range(8):
            if data[x+i][y+j] != start_W[i][j]:
                count_W += 1
            if data[x+i][y+j] != start_B[i][j]:
                count_B += 1
    return min(count_W, count_B)


result = float('inf')
for i in range(N-7):
    for j in range(M-7):
        result = min(result, count_color(i, j))

print(result)
