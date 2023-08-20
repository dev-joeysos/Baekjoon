from collections import deque
N = int(input())
numbers = list(map(int, input().split()))
d = deque([(idx+1, num) for idx, num in enumerate(numbers)])

order = []
while True:
    idx, tmp = d.popleft()
    order.append(idx)
    if not d:
        break
    if tmp > 0:
        for i in range(tmp-1):
            x = d.popleft()
            d.append(x)
    elif tmp < 0:
        for i in range(abs(tmp)):
            x = d.pop()
            d.appendleft(x)
print(' '.join(map(str, order)))
