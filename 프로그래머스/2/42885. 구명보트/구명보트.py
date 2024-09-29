from collections import deque

def solution(people, limit):
    answer = 0
    people = deque(sorted(people)) # list to deque
    
    while(people):
        # 한 명만 남는 경우 혼자 태워서 구출
        if len(people) == 1:
            answer += 1
            break
        
        # 가장 무거운 사람과 가장 가벼운 사람 둘이 나가지는 경우 구출함
        if people[0] + people[-1] <= limit:
            people.popleft()
            people.pop()
        # 무거운 애 밖에 못 나가는 경우
        else:
            people.pop()
        
        answer += 1
    
    return answer