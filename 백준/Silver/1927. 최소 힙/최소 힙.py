import heapq, sys

heap = []
n = int(sys.stdin.readline())

for _ in range(n):
    number = int(sys.stdin.readline())
    if not number: # 0
        min_value = heapq.heappop(heap) if heap else 0
        print(min_value)
    else:
        heapq.heappush(heap, number)