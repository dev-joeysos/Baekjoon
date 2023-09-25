def solution(s):
    stack = []

    for i in s:
        if i == '(':
            stack.append(i)
        else:
            if not stack:
                return False
            stack.pop()
    if len(stack) == 0:
        answer = True
    else:
        answer = False

    return answer

'''
괄호 검사
스택 생각
(면 넣고 )면 pop 하자'''