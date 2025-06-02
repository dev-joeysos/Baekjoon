N,M=map(int,input().split())
S={}
for _ in range(N):
    url,pw=map(str,input().split())
    S[url]=pw

for _ in range(M):
    name=input()
    print(S[name])