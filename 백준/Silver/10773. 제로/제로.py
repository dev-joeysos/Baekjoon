K = int(input())
stack = []
for _ in range(K):
    tmp = int(input())
    if tmp == 0 and len(stack) > 0:
        stack.pop()
    else:
        stack.append(tmp)
sum = sum(stack)
print(sum)