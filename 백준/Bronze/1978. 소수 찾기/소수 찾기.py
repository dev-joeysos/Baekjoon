# 1 일 1 백준
# 230801
# 1978 번

# 소수 찾기
# 약수를 빼면 되지

N = int(input())
num_list = []
discount = 0

num_list = list(map(int, input().strip().split()))


for num in num_list:
    if num == 1:
        discount += 1
    else:
        for j in range(2, num):
            if num % j == 0:  # 소수가 아닌 경우
                discount += 1
                break
R = N - discount
print(R)
