N, B = input().split()
B = int(B)
result = 0
power = 0

for item in N[::-1]:
    if item.isdigit():
        item = int(item)
    else:
        item = item.upper()
        item = ord(item) - ord('A') + 10  # A=10, B=11, ..., Z=35로 변환
    result += item * (B ** power)
    power += 1

print(result)
