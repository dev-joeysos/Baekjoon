def solution(a, b):
    answer = 0
    A = int(str(a[0])+str(a[1])+str(a[2]))
    B = int(str(b[0])+str(b[1])+str(b[2]))
    if A < B:
        answer = 1
    return answer