def fac(n):
    s=1
    for i in range(n,0,-1):
        s*=i
    return s

N=int(input())
cnt=0
for i in str(fac(N))[::-1]:
    if i!='0':
        print(cnt)
        break    
    cnt+=1