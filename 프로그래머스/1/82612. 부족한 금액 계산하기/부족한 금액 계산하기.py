def solution(p, m, c):
    tmp = 0
    for i in range(1,c+1):
        tmp += p*i
    ans = m - tmp
    if ans <= 0:
        return abs(ans)
    else:
        return 0