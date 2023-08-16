def gcd(n, m):
    while m:
        n, m = m, n % m
    return n


def _gcd(lst):
    result = lst[0]
    for num in lst[1:]:
        result = gcd(result, num)
    return result


N = int(input())

garosu = []
for _ in range(N):
    x = int(input())
    garosu.append(x)

ganguk = []
for i in range(N - 1):
    tmp = garosu[i+1] - garosu[i]
    ganguk.append(tmp)

gcd = _gcd(ganguk)

count = 0
for num in ganguk:
    num = num // gcd - 1
    count += num

print(count)