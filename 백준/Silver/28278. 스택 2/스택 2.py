'''
understanding stack with python
'''
import sys
input = sys.stdin.readline
N = int(input())
X_stack = []

for _ in range(N):
    tmp = list(map(int, input().split()))

    if tmp[0] == 1:
        X_stack.append(tmp[1])
    elif tmp[0] == 2:
        if len(X_stack) == 0:
            print("-1")
        else:
            top = X_stack.pop()
            print(top)
    elif tmp[0] == 3:
        print(len(X_stack))
    elif tmp[0] == 4:
        if len(X_stack) == 0:
            print("1")
        else:
            print("0")
    else:  # 5
        if len(X_stack) != 0:
            top = X_stack[-1]
            print(top)
        else:
            print("-1")
