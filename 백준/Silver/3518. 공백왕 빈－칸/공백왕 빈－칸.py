import sys

lines = []
for line in sys.stdin:
    lines.append(line.strip().split())

max_col = max(len(row) for row in lines)
max_width = [0] * max_col

for row in lines:
    for i in range(len(row)):
        max_width[i] = max(max_width[i], len(row[i]))

for row in lines:
    for i in range(len(row)):
        word = row[i]
        print(word, end='')
        if i != len(row) - 1:
            print(' ' * (max_width[i] - len(word) + 1), end='')  # +1 for space
    print()