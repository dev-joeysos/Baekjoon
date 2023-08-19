import sys
input = sys.stdin.readline
for i in range(int(input())):
    stack = []
    for i in input().rstrip():
        if i == "(":
            stack.append(i)
        else:
            try:
                stack.pop()
            except:
                print("NO")
                break
                # 괄호를 열기도 전에 닫음
    else:
        print("NO" if stack else "YES")
        # 스택이 안 비어있는 경우 NO 출력