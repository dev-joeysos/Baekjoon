T=int(input())

for _ in range(T):
    H,W,N=map(int,input().split())
    
    if N%H==0:
        q=N//H
        r=H
    else:
        q=N//H+1
        r=N%H
    
    if q<10:
        ans=f'{r}0{q}'
    else:
        ans=f'{r}{q}'
    print(ans)