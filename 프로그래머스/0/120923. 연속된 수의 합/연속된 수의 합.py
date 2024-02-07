def solution(num, total):
    answer = []
    
    '''
    num개의 수의 합이 total과 같은지를 확인하는 문제
    start, start+1, start+2, ... start+num-1
    = num*start + num*(num-1)//2
    
    start를 어떻게 결정할 것인가?
    num이 홀수인 경우
        total // num = 가운데 수
        start = total // num - num // 2
    num이 짝수인 경우
        total // num = 가운데 바로 옆수
        start = total // num - num // 2 + 1
    '''
    start = 0
    # num이 홀수
    if num%2:
        start = total // num - num // 2
    # num이 짝수
    else:
        start = total // num - num // 2 + 1

    for i in range(start, start + num):
        answer.append(i)
    return answer