X = int(input())
i = 1

while X > i:
    X -= i
    i += 1

if i % 2 == 0:
    numerator = X
    denominator = i - X + 1
else:
    numerator = i - X + 1
    denominator = X

print(str(numerator) + '/' + str(denominator))
