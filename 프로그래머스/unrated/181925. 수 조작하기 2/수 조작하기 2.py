def solution(L):
    answer = ''
    # L = [1,2,3,4]
    for i in range(len(L)-1):
        x = L[i+1] - L[i]
        if x == 1:
            answer += 'w'
        elif x == -1:
            answer += 's'
        elif x == 10:
            answer += 'd'
        else:
            answer += 'a'
    return answer