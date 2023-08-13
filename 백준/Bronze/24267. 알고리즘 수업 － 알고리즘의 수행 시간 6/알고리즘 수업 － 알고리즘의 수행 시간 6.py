n = int(input())

count = 0
for i in range(1, n-1):
    count += (n-i) * (n-i-1) // 2

print(count)
print(3)  # 최고차항의 차수
