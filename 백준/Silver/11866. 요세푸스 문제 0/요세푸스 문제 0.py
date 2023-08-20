import queue
queue = queue.Queue()
N, K = map(int, input().split())
for i in range(1, N+1):
    queue.put(i)
order = []
while not queue.empty():
    for i in range(K-1):
        tmp = queue.get()
        queue.put(tmp)
    tmp = queue.get()
    order.append(tmp)
print('<' + ', '.join(map(str, order)) + '>')
