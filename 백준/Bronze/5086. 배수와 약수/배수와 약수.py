# 1 일 1 백준
# 230801
# 5086 번

# 배수와 약수
while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    if b % a == 0:
        print('factor')
    elif a % b == 0:
        print('multiple')
    else:
        print('neither')
