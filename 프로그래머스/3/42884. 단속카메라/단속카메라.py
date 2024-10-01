from collections import deque 

def solution(routes):
    answer = 0
    routes.sort(key = lambda x: x[1]) # 비교 기준이 종료 시점입니다.
    deq = deque(routes)

    route = deq.popleft()
    initial_camera = route[1]
    answer += 1
    
    while deq:
        route = deq.popleft()
        entry = route[0]
        end = route[1]
        
        if entry <= initial_camera:
            continue
        else:
            initial_camera = end
            answer += 1

    return answer