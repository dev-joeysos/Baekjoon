import sys, math
input = sys.stdin.readline

def main():
    n = int(input())
    # n이 제곱수인 경우: 가능한 쌍이 무한 → -1
    if math.isqrt(n)**2 == n:
        print(-1)
        return

    # Case 1: n = a^2 + b^2 (√n이 빗변)
    cnt1 = 0
    limit1 = math.isqrt(n // 2)
    for a in range(1, limit1 + 1):
        b2 = n - a*a
        b = math.isqrt(b2)
        if b*b == b2:
            cnt1 += 1

    # Case 2: n = (b - a)(b + a) (√n이 빗변 아님)
    cnt2 = 0
    limit2 = math.isqrt(n)
    for d in range(1, limit2 + 1):
        if n % d == 0:
            e = n // d
            # d < e, (d+e)가 짝수인 약수 쌍만 카운트
            if d < e and (d + e) % 2 == 0:
                cnt2 += 1

    print(cnt1 + cnt2)

if __name__ == "__main__":
    main()