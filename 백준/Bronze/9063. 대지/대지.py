# 1 일 1 백준
# 230802
x_dot = []
y_dot = []
N = int(input())
for i in range(N):
    x, y = map(int, input().split())
    x_dot.append(x)
    y_dot.append(y)

X = max(x_dot) - min(x_dot)
Y = max(y_dot) - min(y_dot)

print(X*Y)
