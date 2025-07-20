# 신발끈 공식, 벡터외적, 기하
import sys
input=sys.stdin.readline

def shoelace(pos):
    result=0
    for i in range(len(pos)):
        cx,cy=pos[i]
        if i==len(pos)-1:
            nx,ny=pos[0]
        else:
            nx,ny=pos[i+1]
        result+=cx*ny-nx*cy
    result/=2
    
    return abs(result)
    
def main():
    n=int(input())
    pos=[list(map(int,input().split())) for _ in range(n)]
    print(f'{shoelace(pos):.1f}')
    
if __name__=="__main__":
    main()