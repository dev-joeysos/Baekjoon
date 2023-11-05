def solution(n):
    answer = 0
    tmp = int(n**(1/2))
    
    if tmp**2 == n:
        return (tmp+1)**2
    else:
        return -1