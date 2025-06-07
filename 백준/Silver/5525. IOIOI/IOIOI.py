import sys
input=sys.stdin.readline
n=int(input())
m=int(input())
s=str(input())

i=1
cnt=0
answer=0
while i<m-1:
    if s[i-1]=='I' and s[i]=='O' and s[i+1]=='I':
        cnt+=1
        if cnt>=n:
            answer+=1
        i+=2
    else:
        cnt=0
        i+=1

print(answer)