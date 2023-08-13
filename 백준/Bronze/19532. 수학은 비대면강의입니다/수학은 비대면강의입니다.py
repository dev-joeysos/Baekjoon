# 수학은 비대면 강의입니다.

arr = list(map(int, input().split()))
a, b, c, d, e, f = arr[0], arr[1], arr[2], arr[3], arr[4], arr[5]

y = int((c*d-a*f)/(b*d-a*e))
x = int((c*e-b*f)/(a*e-b*d))

print(x, y)