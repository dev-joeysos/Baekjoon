'''
정수의 순서를 바꾸지 않고 적절히 더하거나 빼서 타겟 넘버를 만들려고 합니다
더하고 빼는 방법의 수를 반환합니다.
숫자의 순서는 바뀌지 않습니다
'''
# BFS
def solution(numbers, target):
    answer = 0
    leaves = [0]
    
    for num in numbers:
        temp = []
        for parent in leaves:
            temp.append(parent+num)
            temp.append(parent-num)
        leaves = temp
    for leaf in leaves:
        if leaf == target:
            answer += 1
    return answer