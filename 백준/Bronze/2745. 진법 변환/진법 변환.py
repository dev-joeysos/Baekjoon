N, B = input().split()
B = int(B)
result = 0

for char in N:
    result = B * result + (int(char) if char.isdigit() else (10 + ord(char.upper()) - ord('A')))

print(result)
