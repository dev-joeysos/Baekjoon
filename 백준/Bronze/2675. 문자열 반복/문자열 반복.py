T = int(input())

for i in range(T):
    R, S = input().split()  # 공백을 기반으로 분리하는 분류 조건
    R = int(R)
    S = list(S)  # 정수형, 리스트형 형변환

    for k in range(len(S)):
        S[k] = S[k]*R

    print(''.join(S))