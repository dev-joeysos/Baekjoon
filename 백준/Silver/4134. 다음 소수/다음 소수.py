import math

def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(num)) + 1, 2):  # 홀수만 검사
        if num % i == 0:
            return False
    return True

T = int(input())

for _ in range(T):
    n = int(input())
    while not is_prime(n):
        n += 1
    print(n)
