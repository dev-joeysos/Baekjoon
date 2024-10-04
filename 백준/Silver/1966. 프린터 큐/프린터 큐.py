from collections import deque

t = int(input())  # 테스트 케이스 수 입력
for _ in range(t):
    n, m = map(int, input().split())  # n은 문서 수, m은 궁금한 문서의 인덱스
    queue = deque(enumerate(map(int, input().split())))  # (인덱스, 중요도) 형태로 deque 생성
    
    count = 0
    while True:
        if queue[0][1] == max(queue, key=lambda x: x[1])[1]:  # 중요도가 가장 높은 문서가 맨 앞에 있는지 확인
            count += 1
            if queue[0][0] == m:  # 인덱스가 m이면 결과 출력 후 종료
                print(count)
                break
            else:
                queue.popleft()  # 출력했으니 제거
        else:
            queue.append(queue.popleft())  # 중요도가 낮으면 맨 뒤로 보냄
