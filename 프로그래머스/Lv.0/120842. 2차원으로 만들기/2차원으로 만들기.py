def solution(lst, n):
    answer = []
    N = len(lst) // n
    for i in range(N):
        answer.append(lst[i*n:i*n+n:])
    return answer