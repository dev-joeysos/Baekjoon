# 모두 같은 숫자인지 확인
def is_same(lst,x,y,size):
    base=lst[x][y]
    for i in range(x,x+size):
        for j in range(y,y+size):
            if base != lst[i][j]:
                return False
    else:
        return True

# recursion
def recurse(paper,x0,y0,N,ans):    
    if is_same(paper,x0,y0,N):
        ans[paper[x0][y0]]+=1
        return ans

    size=N//2
    x1,y1=x0+size,y0+size
    x2,y2=x0,y1
    x3,y3=x1,y0
        
    ans=recurse(paper,x0,y0,size,ans)
    ans=recurse(paper,x1,y1,size,ans)
    ans=recurse(paper,x2,y2,size,ans)
    ans=recurse(paper,x3,y3,size,ans)
    
    return ans

import sys
input=sys.stdin.readline
N=int(input())
paper=[list(map(int,input().split())) for _ in range(N)]

ans=[0,0]
recurse(paper,0,0,N,ans)

print(ans[0])
print(ans[1])