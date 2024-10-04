import sys, heapq

n = int(sys.stdin.readline())
heap = []

for _ in range(n):
    number = int(sys.stdin.readline())
    if not number:
        if not heap:
            print(0)
        else:
            print(-heapq.heappop(heap))
    else:
        heapq.heappush(heap, -number)