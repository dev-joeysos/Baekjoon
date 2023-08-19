while True:
    string = input()
    stack = []

    if string == '.':
        break
    for item in string:
        if item == '(' or item == '[':
            stack.append(item)
        elif item == ']':
            if len(stack) != 0 and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(']')
        elif item == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(')')

    if len(stack) == 0:
        print('yes')
    else:
        print('no')
