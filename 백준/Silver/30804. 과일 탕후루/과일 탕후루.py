#two pointer
#defaultdict 
from collections import defaultdict
import sys
input=sys.stdin.readline
n=int(input())
fruits=list(map(int,input().split()))
fruits_count=defaultdict(int)
start,end=0,0
max_len=0
for end in range(n):
    fruit=fruits[end]
    fruits_count[fruits[end]]+=1 #과일추가
    
    while len(fruits_count)>2: 
        fruits_count[fruits[start]]-=1
        if fruits_count[fruits[start]]==0:
            del fruits_count[fruits[start]]
        start+=1
    
    max_len=max(max_len,end-start+1)

print(max_len)