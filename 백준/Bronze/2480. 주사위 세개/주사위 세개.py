a, b, c = map(int, input().split())

if a == b == c:  # 모든 눈이 같은 경우
    prize = 10000 + a * 1000
elif a == b or a == c:  # 두 개의 눈이 같은 경우 1
    prize = 1000 + a * 100
elif b == c:  # 두 개의 눈이 같은 경우 2
    prize = 1000 + b * 100
else:  # 모든 눈이 다른 경우
    prize = max(a, b, c) * 100

print(prize)
