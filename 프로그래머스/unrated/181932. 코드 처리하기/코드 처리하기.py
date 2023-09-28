def solution(code):
    answer = ''
    mode = 0
    for i in range(len(code)):
        if mode == 0:
            if code[i] != '1':
                if i % 2 == 0:
                    answer += code[i]
            else:
                mode = 1
        else:
            if code[i] != '1':
                if i % 2 == 1:
                    answer += code[i]
            else:
                mode = 0
    if len(answer) == 0:
        answer = 'EMPTY'
    return answer