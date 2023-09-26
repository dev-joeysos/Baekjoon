def solution(num_list):
    answer = 0
    for num in num_list:
        if num < 0:
            answer = num_list.index(num)
            break
        else:
            answer = -1
    return answer