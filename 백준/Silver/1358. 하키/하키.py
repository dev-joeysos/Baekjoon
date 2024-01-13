# 1일 1백준
# 두 점 사이의 거리
def dist(x, y, a, b):
    return (x - a) ** 2 + (y - b) ** 2


W, H, X, Y, P = map(int, input().split())
radius = H // 2
r = radius ** 2
p = 0
for i in range(P):
    x, y = map(int, input().split())
    r1 = dist(x, y, X, Y + radius)
    r2 = dist(x, y, X + W, Y + radius)
    # 직사각형
    if X <= x <= X + W:
        if Y <= y <= Y + H:
            p += 1
    # 왼쪽 반원
    elif r1 <= r:
        p += 1
    # 오른쪽 반원
    elif r2 <= r:
        p += 1
    else:
        continue
print(p)
