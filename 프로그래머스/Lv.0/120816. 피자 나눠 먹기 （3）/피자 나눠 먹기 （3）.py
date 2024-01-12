def solution(s, n):
    ans = 0
    cnt = n//s
    remain = n%s
    if remain != 0:
        ans = cnt+1
    else:
        ans = cnt
    return ans