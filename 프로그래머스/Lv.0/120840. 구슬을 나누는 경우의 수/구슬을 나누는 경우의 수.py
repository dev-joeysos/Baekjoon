def factorial(n):
    rst = 1
    while n > 0:
        rst *= n
        n -= 1
    return rst

def solution(balls, share):
    return factorial(balls) / (factorial(balls - share) * factorial(share))