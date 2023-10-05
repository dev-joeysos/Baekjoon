def solution(rny_string):
    answer = ''
    for rny in rny_string:
        if rny == 'm':
            answer += 'rn'
        else:
            answer += rny
    return answer