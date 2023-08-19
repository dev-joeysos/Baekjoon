N = int(input())  # 사람의 수
line = list(map(int, input().split()))  # 대기열의 번호표 순서
stack = []  # 1열 공간
i = 1  # 현재 통과해야 하는 번호

for num in line:
    while stack and stack[-1] == i:  # 스택의 맨 위 사람이 현재 번호와 일치하면 통과
        stack.pop()
        i += 1

    if num == i:  # 대기열의 맨 앞 사람이 현재 번호와 일치하면 통과
        i += 1
    else:  # 아니라면 1열 공간으로 이동
        stack.append(num)

# 남아있는 스택 내의 사람들도 통과할 수 있는지 확인
while stack and stack[-1] == i:
    stack.pop()
    i += 1

# 스택이 비어 있으면 모든 사람이 통과한 것
if not stack:
    print("Nice")
else:
    print("Sad")
