def gcd(n, m):
    while m:
        n, m = m, n % m
    return n


def lcm(n, m):
    return n * m // gcd(n, m)


a, b = map(int, input().split())
c, d = map(int, input().split())

e = lcm(b, d)
f = a * (e // b) + c * (e // d)

g = gcd(e, f)
e = e // g
f = f // g
print(f, e)