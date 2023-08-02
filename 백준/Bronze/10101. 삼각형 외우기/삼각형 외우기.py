# 1 일 1 백준
# 230802
N = []
for i in range(3):
    n = int(input())
    N.append(n)
a = N[0]
b = N[1]
c = N[2]

if a+b+c == 180:
    if a == 60 and b == 60 and c == 60:
        print("Equilateral")
    elif a == b or b == c or a == c:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Error")
