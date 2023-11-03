def solution(str_list):
    answer = []
    for idx, val in enumerate(str_list):
        if val == "l":
            return str_list[:idx]
        elif val == "r":
            return str_list[idx+1:]
    return answer