N=int(input())
lst=[]
for _ in range(N):
    x,y=map(int,input().split())
    lst.append([x,y])

ans=[]
for i in range(len(lst)):
    x,y=lst[i][0],lst[i][1]
    rank=1
    for j in range(len(lst)):
        dx,dy=lst[j][0],lst[j][1]
        
        if x<dx and y<dy:
            rank+=1
        else:
            continue
        #print('x,y,dx,dy:,rank', x,y,dx,dy,rank)
        
    ans.append(rank)

#print(' '.join(map(str,ans)))
print(*ans)