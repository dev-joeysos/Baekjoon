def solution(citiation):
    answer = 0
    n = len(citiation)
    citiation.sort(reverse=True)
    for num, cit in enumerate(citiation):
        if cit >= num+1:
            h_index = num+1
            answer = h_index
    return answer