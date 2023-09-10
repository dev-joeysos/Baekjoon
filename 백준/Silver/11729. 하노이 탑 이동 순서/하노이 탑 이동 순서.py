
def move(s, to):
    print(s, to)


def hanoi(N, s, f, m):  # s,m,f == list
    if N == 1:
        move(s, f)
        return
    else:
        hanoi(N-1, s, m, f)
        move(s, f)
        hanoi(N-1, m, f, s)


N = int(input())
K = 2**N-1
print(K)
hanoi(N, 1, 3, 2)