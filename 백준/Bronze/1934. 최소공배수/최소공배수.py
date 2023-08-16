#유클리드 알고리즘
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


T = int(input())
num = []
for _ in range(T):
    A, B = map(int, input().split())
    print(lcm(A, B))