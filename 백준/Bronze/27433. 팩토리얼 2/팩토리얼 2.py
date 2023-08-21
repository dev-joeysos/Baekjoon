# 재귀 사용해서 풀기

N = int(input())


def factorial(result, N):
    if N == 0:
        print(result)
    else:
        result *= N
        factorial(result, N-1)


factorial(1, N)
