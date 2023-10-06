def solution(s):
    answer = ''
    for i in s:
        if ord(i) < ord('l'):
            answer += 'l'
        else:
            answer += i 
    return answer