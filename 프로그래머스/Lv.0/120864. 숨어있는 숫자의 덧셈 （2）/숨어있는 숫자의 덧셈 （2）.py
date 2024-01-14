def solution(ms):
    answer = ''
    for m in ms:
        if m.isdigit():
            answer += m
        else:
            answer += ' '
    return sum(list(map(int, answer.split())))