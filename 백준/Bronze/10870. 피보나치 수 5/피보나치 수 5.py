# 재귀 사용해서 풀기
def fibonacci(n):
    if n >= 2:
        return fibonacci(n-1) + fibonacci(n-2)
    elif n == 1:
        return 1
    else:
        return 0


n = int(input())
print(fibonacci(n))
