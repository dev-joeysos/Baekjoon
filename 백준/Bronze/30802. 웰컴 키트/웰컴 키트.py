N=int(input())
S=map(int,input().split())
T,P=map(int,input().split())

total=0
for s in S:
    total+=(s-1)//T+1
    
quo=N//P
rem=N%P

print(total)
print(quo,rem)