N = int(input())
line = list(map(int, input().split()))
stack = []
i = 1
for num in line:
    if num == i:
        i += 1
    else:
        stack.append(num)
    while stack and stack[-1] == i:  # 공간에 들어간 top이 다음 순서로 간식을 받는 경우
        stack.pop()
        i += 1

if not stack:
    print("Nice")
else:
    print("Sad")