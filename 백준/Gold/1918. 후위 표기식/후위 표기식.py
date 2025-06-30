'''
수식의 표기법

후위표기법
-장점:순서조절, 괄호없음

중위표기식->후위표기식
1.중위표기신의 연산자의 우선순위에 따라 괄호로 묶는다.
2.괄호 안의 연산자를 괄호의 오른쪽으로 옮겨준다.
중위표기식을 후위표기식으로 고치는 프로그램 작성
연산자 우선순위는 ((,))(*,/) (+,-) 겠죠?

''' 
import sys
input=sys.stdin.readline
infix=input().strip()
stack=[]
operators='+-*/()'
priority={
    '(':0,
    '+':1,
    '-':1,
    '*':2,
    '/':2
}

for char in infix:
    # 연산자인 경우
    if char in operators:
        if char=='(':
            stack.append(char)
        elif char==')':
            while True:
                stack_top=stack.pop()
                if stack_top=='(':
                    break
                print(stack_top,end='')
        elif char in priority:
            while stack and priority[char]<=priority[stack[-1]]: #연산자 우선순위가 더 낮은 경우
                stack_top=stack.pop()
                print(stack_top,end='')
            stack.append(char)    
    #연산자가 아닌경우
    else:
        print(char,end='')

while stack:
    print(stack.pop(),end='')