import sys
input=sys.stdin.readline
M=int(input())

S=set()
for _ in range(M):
    parts=input().split()
    if parts[0]=='add':
        S.add(int(parts[1]))
    elif parts[0]=='remove':
        S.discard(int(parts[1]))
    elif parts[0]=='check':
        print(1 if int(parts[1]) in S else 0) 
    elif parts[0]=='toggle':
        S.discard(int(parts[1])) if int(parts[1]) in S else S.add(int(parts[1]))
    elif parts[0]=='all':
        S=set(i for i in range(1,21))
    elif parts[0]=='empty':
        S=set()