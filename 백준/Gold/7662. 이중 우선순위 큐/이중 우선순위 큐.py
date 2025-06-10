#dual priority queue
from collections import defaultdict
import sys,heapq
input=sys.stdin.readline
t=int(input())
for _ in range(t):
    k=int(input())
    min_heap=[]
    max_heap=[]
    dict=defaultdict(int)
    for _ in range(k):
        op,val=input().split()
        val=int(val)
        
        if op=='I':
            heapq.heappush(min_heap,val)
            heapq.heappush(max_heap,-val)
            dict[val]+=1
        elif op=='D':
            heap=max_heap if val==1 else min_heap
            while heap:
                poped_val=-heapq.heappop(heap) if val==1 else heapq.heappop(heap)
                if dict[poped_val]>0:#유효성 검증
                    dict[poped_val]-=1
                    break
    
    #힙의 유효값 정리
    while max_heap and dict[-max_heap[0]]==0:
        heapq.heappop(max_heap)
    while min_heap and dict[min_heap[0]]==0:
        heapq.heappop(min_heap)
        
    #정리 후 값의 여부 따라서 출력
    if not max_heap or not min_heap:
        print('EMPTY')
    else:
        print(-max_heap[0],min_heap[0])