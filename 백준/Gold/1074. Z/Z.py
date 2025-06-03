import sys
input=sys.stdin.readline
n,r,c=map(int,input().split())

def z(x,y,size,cnt):
    if size==2:
        for dx,dy in [(0,0),(0,1),(1,0),(1,1)]:
            nx,ny=x+dx,y+dy
            if nx==r and ny==c: #target condtion
                return cnt
            cnt+=1
        return cnt # 못 찾으면 반환
    
    half=size//2
    area=half*half
    
    if r<x+half and c<y+half:
        return z(x,y,half,cnt) #z0
    elif r<x+half and c>=y+half:
        return z(x,y+half,half,cnt+area) #z1
    elif r>=x+half and c<y+half:
        return z(x+half,y,half,cnt+area*2) #z2
    elif r>=x+half and c>=y+half:
        return z(x+half,y+half,half,cnt+area*3) #z3

print(z(0,0,2**n,0))