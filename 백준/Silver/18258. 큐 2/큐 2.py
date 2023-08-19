'''
understanding of queue(FIFO)

'''
import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
Q = deque()
for _ in range(N):
    x = input().split()
    if x[0] == 'push':
        Q.append(x[1])
    elif x[0] == 'pop':
        if len(Q) == 0:
            print('-1')
        else:
            tmp = Q.popleft()
            print(tmp)
    elif x[0] == 'size':
        print(len(Q))
    elif x[0] == 'empty':
        if len(Q) == 0:
            print('1')
        else:
            print('0')
    elif x[0] == 'front':
        if len(Q) == 0:
            print('-1')
        else:
            print(Q[0])
    elif x[0] == 'back':
        if len(Q) == 0:
            print('-1')
        else:
            print(Q[-1])
