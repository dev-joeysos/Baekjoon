'''
상대 팀 진영에 최대한 빨리 도착하는 것이 유리합니다.
맵이 있어요
상대팀 진영에 도착하지 못하는 경우도 존재합니다.
1인 경우에 길이 열리고, 0이면 막혀있는 것입니다.
bfs를 구현하기 위해 덱에서 넣고 빼며, 도착지점에 도달할 때까지 계속 뺍니다.
'''
from collections import deque

def solution(maps):
    answer = 0
    # 동서남북 방향벡터
    dx = [1, -1, 0, 0] 
    dy = [0, 0, 1, -1]
    
    # 범용성을 고려해 map을 더 일반화합시다.
    n = len(maps)
    m = len(maps[0])

    # 방문 여부를 기록합니다.
    visited = [[False] * m for _ in range(n)]

    # bfs 와 map 에선 덱을 사용합시다.
    queue = deque([(0, 0, 1)]) # x, y, dist
    visited[0][0] = True
    
    while queue:
        x, y, dist = queue.popleft()
        
        # 상대팀 진영에 도착한 경우
        if x == n-1 and y == m-1:
            return dist
        
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            # 이동한 위치가 maps 상에 존재하고, 길이 열려있는 경우(1)
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny, dist + 1))
        
    # 도착하지 못하는 경우
    return -1