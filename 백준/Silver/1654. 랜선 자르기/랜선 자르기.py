# 랜선 자르기
def cond(num, n, lst):
    s=0
    for i in lst:
       s+=i//num
    if s>=n:
        return True
    else:
        return False

K,N=map(int,input().split())
L=sorted([int(input()) for _ in range(K)])

start=1
end=max(L)
ans=0
while start<=end:
    mid=(start+end)//2
    if cond(mid,N,L):
        start=mid+1
        ans=mid
    else:
        end=mid-1
print(ans)