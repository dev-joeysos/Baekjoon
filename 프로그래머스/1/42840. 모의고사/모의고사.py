'''
수포자는 수학을 포기한 사람의 준말이다.
전부 찍는다
1번 부터 마지막 문제까지 찍는 방식이 다름
1번 수포자는 12345 12345
2번 21232425 반복
3번 3311224455 반복

정답이 주어지면 가장 문제를 많이 맞힌 사람은 누구게
여럿이면 여럿 return 하기
'''

def solution(answers):
    n1 = [1,2,3,4,5]
    n2 = [2,1,2,3,2,4,2,5]
    n3 = [3,3,1,1,2,2,4,4,5,5]
    
    a = 0
    cnt1, cnt2, cnt3 = 0,0,0

    for i in answers:
        if i == n1[a%5]:
            cnt1 += 1
        if i == n2[a%8]:
            cnt2 += 1
        if i == n3[a%10]:
            cnt3 += 1
        a += 1
        
    answer, lst = [], []

    lst.append(cnt1)
    lst.append(cnt2)
    lst.append(cnt3)
    
    for i, l in enumerate(lst):
        if max(lst) == l:
            answer.append(i+1)
    return answer