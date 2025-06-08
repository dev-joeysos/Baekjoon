from collections import deque
import sys
input=sys.stdin.readline

def parsing(s): #'[1,2,3]' → deque([1,2,3])
    if s.strip()=='[]':
        return deque()
    return deque(map(int, s.strip()[1:-1].split(',')))

t=int(input())
for _ in range(t):
    p=input().rstrip()
    n=int(input().rstrip())
    numbers=parsing(str(input()).rstrip())
    
    is_reversed=False
    error_flag=False

    for cmd in p:
        if cmd=='R':
            is_reversed=not is_reversed
        elif cmd=='D':
            if not numbers:
                print('error')
                error_flag=True
                break
            if is_reversed:
                numbers.pop()
            else:
                numbers.popleft()
    
    if error_flag:
        continue
    
    if is_reversed:
        numbers.reverse()

    print(f"[{','.join(map(str,numbers))}]")
