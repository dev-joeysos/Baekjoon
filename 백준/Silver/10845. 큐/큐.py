import sys
input = sys.stdin.readline
n = int(input())
q = []
for _ in range(n):
    word = input().split()
    w0 = word[0]
    if w0 == "push":
        q.append(word[1])
    elif w0 == "pop":
        if len(q) == 0:
            print(-1)
        else:
            x = q.pop(0)
            print(x)
    elif w0 == "size":
        print(len(q))
    elif w0 == "empty":
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif w0 == "front":
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])
    elif w0 == "back":
        if len(q) == 0:
            print(-1)
        else:
            print(q[-1])
