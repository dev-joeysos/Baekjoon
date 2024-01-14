def solution(eg):
    answer = []
    g = eg.copy()
    g.sort(reverse=True)
    for e in eg:
        answer.append(g.index(e)+1)
    return answer