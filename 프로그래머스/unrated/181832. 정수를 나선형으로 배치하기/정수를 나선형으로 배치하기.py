def solution(n):
   
    #[[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]] 빈 리스트 만들기
    sprial = [[0] * n for _ in range(n)]
   
    # 무언가에 부딪혔을 때 [우 하 상 좌]순으로 움직이게 하는 방향설정
    # [ 오른쪽으로(→) 이동 / 부딪히면 아래로(↓) 이동 / 부딪히면 왼쪽(←)으로 이동 / 부딪히면 위로(↑) 이동 ] 반복  
    dx = [1,0,-1,0] # 처음 방향은 오른쪽이니 dx는 1, dy는 0 / 부딪히면 아래쪽으로 이동해야 하니 dx 0 dy 1 이런식
    dy = [0,1,0,-1]
   
    #처음 좌표
    x, y = 0, 0
   
    #방향 (dx, dy의 0,1,2,3 0,1,2,3 대입하면서 방향을 설정하는 용도)
    diretion = 0
   
    # n의 제곱만큼 반복 (i는 1부터 n*n까지)
    for i in range(1,(n*n)+1):
       
        #빈배열에 i 순서대로 넣어주기
        sprial[y][x] = i
       
        #이동할 다음 좌표 구하기
        nx = x + dx[diretion]
        ny = y + dy[diretion]
       
        #이동할 좌표가 벽에 부딪히거나(인덱스를 벗어나는 행위) 숫자가 들어있을 시 다음 이동할 좌표 새로 구하기
        if nx >= n or nx < 0 or ny >= n or ny < 0 or sprial[ny][nx] != 0:
           
            #방향은 총 상하좌우 4가지
            diretion = (diretion + 1) % 4
           
            #방향 정한후 다음 이동할 좌표 정하기
            nx = x + dx[diretion]
            ny = y + dy[diretion]
       
        #x, y에 이동해야할 다음 좌표 넣기
        x, y = nx, ny
       
    return sprial