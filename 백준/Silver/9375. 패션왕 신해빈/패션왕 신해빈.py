import sys
input=sys.stdin.readline

T=int(input())
for _ in range(T):
    d={}
    n=int(input())
    for _ in range(n):
        name,type=input().split()
        if type not in d:
            d[type]=0
        d[type]+=1
        
    total=1
    for count in d.values():
        total*=(count+1)
    
    print(total-1)