import sys
input = sys.stdin.readline

s = input().strip()
bomb = input().strip()
stack = []

bomb_len = len(bomb)

for c in s:
    stack.append(c)
    if ''.join(stack[-bomb_len:]) == bomb:
        del stack[-bomb_len:]

result = ''.join(stack)
print(result if result else "FRULA")