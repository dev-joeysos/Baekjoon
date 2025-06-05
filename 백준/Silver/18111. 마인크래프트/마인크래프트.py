import sys
input=sys.stdin.readline
n,m,b=map(int,input().split())
sod=[]
for _ in range(n):
    sod.append(list(map(int,input().split())))
    
sec_add,sec_rm=1,2
sec_min=float('inf')
best_h=0
for h in range(0,257):
    cnt_add,cnt_rm=0,0
    for i in range(n):
        for j in range(m):
            ch=sod[i][j] #current height
            h_diff=abs(h-ch)
            if h>=ch:
                cnt_add+=h_diff #쌓아야하는 블록수
            else:
                cnt_rm+=h_diff #제거해야하는 블록수
    
    if cnt_add>b+cnt_rm: #인벤토리+제거 블록수 합 부족
        continue
    else:
        sec_total=(cnt_add*sec_add)+(cnt_rm*sec_rm)

    if sec_total<sec_min:
        sec_min=sec_total #갱신
        best_h=h
    elif sec_total==sec_min and h>best_h: #높이 갱신 조건
        best_h=h

print(sec_min, best_h)