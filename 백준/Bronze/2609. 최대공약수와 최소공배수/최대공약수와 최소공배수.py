import sys
input = sys.stdin.readline

n, m = map(int, input().split())

# 최대공약수
for i in range(min(n, m), 0, -1):
    if n % i == 0 and m % i == 0:
        print(i)
        break

# 최소공배수
for i in range(max(n, m), n*m + 1):
    if i % n == 0 and i % m == 0:
        print(i)
        break
