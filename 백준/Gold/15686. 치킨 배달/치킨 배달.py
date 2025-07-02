import sys
input=sys.stdin.readline

#거리 측정
def cal_route(starts,goals):
    total_result=0

    for start in starts:
        INF=float('inf')
        result=INF
        start_x,start_y=start[0],start[1]    
        for goal in goals:
            goal_x,goal_y=goal[0],goal[1]
            route=abs(start_x-goal_x)+abs(start_y-goal_y)
            result=min(route,result)
        total_result+=result
        
    return total_result

#치킨집 좌표 중에서 m개를 선택한 모든 조합을 반환하는 함수
def make_combinations(chickens,m):
    result=[]
    selected=[]
    
    def dfs(depth,idx):
        if depth==m:
            result.append(selected[:])
            return
        for i in range(idx,len(chickens)):
            selected.append(chickens[i])
            dfs(depth+1,i+1)
            selected.pop()
        
    dfs(0,0)
    return result

# ---- main ----

n,m=map(int,input().split())
board=[list(map(int,input().split())) for _ in range(n)]
chickens=[]
houses=[]

#좌표 기록
for i in range(n):
    for j in range(n):
        if board[i][j]==1:
            houses.append((i,j))
        elif board[i][j]==2:
            chickens.append((i,j))
        else:
            continue

if len(chickens)==m:
    #거리 측정
    print(cal_route(houses,chickens))
    pass 

#m보다 클 때
if len(chickens)>m:
    #좌표의 조합을 선택->치킨집 좌표 중에서 M개를 선택
    combos=make_combinations(chickens,m)
    INF=float('inf')
    total=INF
    for combo in combos:
        total=min(total,cal_route(houses,combo))
    print(total)