# 1 일 1 백준
# 230802

x, y, w, h = map(int, input().split())
print(min(w-x, x, y, h-y))
