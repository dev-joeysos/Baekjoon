def solution(l, r):
    # 제곱수를 제외한 모든 수의 약수는 짝수 개이다.
    answer = 0
    for i in range(l, r+1):
        if int(i**(0.5)) == i**(0.5):
            answer -= i
        else:
            answer += i
    return answer