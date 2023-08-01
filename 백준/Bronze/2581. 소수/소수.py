# 1 일 1 백준
# 230801
# 2581 번

# 소수

M = int(input())
N = int(input())
prime_list = []
for x in range(M, N+1):
    if x < 2:
        continue
    is_prime = True
    for i in range(2, x):
        if x % i == 0:  # 소수가 아니면
            is_prime = False
            break
    if is_prime:
        prime_list.append(x)

if len(prime_list) == 0:  # 모든 x가 소수가 아니면
    print("-1")
else:
    print(sum(prime_list))
    print(prime_list[0])
