n = int(input())
stack = []
ans = []
now = 1
find = True
for _ in range(n):
    num = int(input())
    while now <= num:
        stack.append(now)
        ans.append('+')
        now += 1
    if stack[-1] == num:
        stack.pop()
        ans.append('-')
    else:  # 불가능한 경우, TOP를 pop해서 봤는데 맞아야 뽑을 수 있을 거 아니냐. 안 맞는다 못 뽑는다.
        find = False

if not find:
    print('NO')
else:
    for i in ans:
        print(i)
