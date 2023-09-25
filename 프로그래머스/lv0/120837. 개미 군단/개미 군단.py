def solution(hp):
    answer = 0
    lst = [5,3,1]
    
    for i in lst:
        answer += hp // i
        hp = hp % i
    
    return answer

'''
군단은 사냥을 원한다.
장 5 병 3 일 1
23 사냥
그리디 기초
'''