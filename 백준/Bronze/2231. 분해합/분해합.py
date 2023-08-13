# 분해합
# 분해합을 제시하고 생성자 출력하기

N = int(input())
i = 1
while True:
    tmp = i
    sum = 0  # 새로운 정수가 들어올 때마다 자리수 합도 초기화
    # 자리수를 구하는 로직 10으로 나눠서 더하면서 줄인다
    while True:
        sum += tmp % 10  # 10으로 나눈 나머지의 합을 반복
        tmp = tmp//10  # 10으로 나눈 몫으로 업데이트
        if tmp == 0:
            break  # 모든 자리가 구해짐

    if N == i + sum:  # 자리수와 자기 자신을 더함
        print(i)
        break

    if i > 10**6:
        print(0)
        break
    i += 1
