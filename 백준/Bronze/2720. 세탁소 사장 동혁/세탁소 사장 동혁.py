iter = int(input())

penny = ['25', '10', '5', '1']
result = []

for i in range(iter):
    x = int(input())
    for j in range(4):
        share = x // int(penny[j])
        x = x % int(penny[j])
        result.append(share)

for i in range(0, len(result), 4):
    for value in result[i:i+4]:
        print(value)
