def solution(ms):
    answer = ''
    s = 'aeiou'
    for m in ms:
        if m not in s:
            answer += m
    return answer