# 1 일 1 백준
# 230801
# 9506 번

# 약수들의 합
while True:
    N = int(input())
    if N == -1:
        break

    M = [i for i in range(1, N) if N % i == 0]
    if N == sum(M):
        expr = " + ".join(map(str, M))
        print(f"{N} = {expr}")
    else:
        print(f"{N} is NOT perfect.")
