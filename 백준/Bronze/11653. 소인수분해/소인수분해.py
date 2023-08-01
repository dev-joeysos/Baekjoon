# 1 일 1 백준
# 230801
# 11654 번

# 소인수 분해

N = int(input())
factor = []
i = 2
while i <= N:
    if N % i == 0:
        factor.append(i)
        N = N/i
    else:
        i += 1

for num in factor:
    print(num)
