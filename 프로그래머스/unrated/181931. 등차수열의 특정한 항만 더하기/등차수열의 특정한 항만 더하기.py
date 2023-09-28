def solution(a, d, included):
    rst = 0
    for i in included:
        if i: 
            rst += a
        a += d
    return rst