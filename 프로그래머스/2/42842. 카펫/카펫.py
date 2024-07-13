'''
전체 카펫의 크기를 기억하지 못한 이슈가..
갈색 격자수 노란색 격자수가 매개변수로 주어집니다.
카펫의 가로, 세로 크기를 배열에 담아서 리턴합니다.

yellow 를 소인수 분해합니다.
소인수 분해해서 만들어지는 조합을 고려해봅시다

if yellow 가로길이 N, 세로길이 M 인 경우
    brown 개수는 2*(N+M+2) 입니다.
    이 조건을 만족하는 조합을 리턴합니다. 
    제한사항에서 N >= M 입니다. 소인수분해하고 절반까지만 탐색하면 되겠네여
'''
def prime_lst(num):
    lst = []
    for i in range(1, int(num**(1/2))+1): # 제곱수까지만 탐색
        if num % i == 0:
            share = num // i
            lst.append([i, share])
    return lst
    
def solution(brown, yellow):
    answer = []
    # test
    numbers = prime_lst(yellow)
    for nums in numbers:
        h = nums[0]
        w = nums[1]
        total = 2*(h+w+2)
        print(h, w, total)
        if total == brown:
            h += 2
            w += 2
            answer.append(w)
            answer.append(h)
            return answer
    
    
    
    return answer