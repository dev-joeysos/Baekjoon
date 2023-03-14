X = int(input())
N = int(input())
total = sum([a*b for a, b in [map(int, input().split()) for _ in range(N)]])
print("Yes" if total == X else "No")