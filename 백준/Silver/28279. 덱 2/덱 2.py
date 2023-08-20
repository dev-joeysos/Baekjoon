from collections import deque
import sys
input = sys.stdin.readline
d = deque()
N = int(input())
for _ in range(N):
    x = list(map(int, input().split()))
    if x[0] == 1:
        d.appendleft(x[1])
    elif x[0] == 2:
        d.append(x[1])
    elif x[0] == 3:
        if d:
            tmp = d.popleft()
            print(tmp)
        else:
            print('-1')
    elif x[0] == 4:
        if d:
            tmp = d.pop()
            print(tmp)
        else:
            print('-1')
    elif x[0] == 5:
        print(len(d))
    elif x[0] == 6:
        if not d:
            print('1')
        else:
            print('0')
    elif x[0] == 7:
        if d:
            print(d[0])
        else:
            print('-1')
    else:
        if d:
            print(d[-1])
        else:
            print('-1')

