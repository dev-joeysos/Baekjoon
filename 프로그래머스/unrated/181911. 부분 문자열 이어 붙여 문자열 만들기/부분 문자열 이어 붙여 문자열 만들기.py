def solution(my_strings, parts):
    answer = ''
    for i in range(len(my_strings)):
        x,y = parts[i][0], parts[i][1]
        tmp = my_strings[i]
        answer += tmp[x:y+1]
    return answer