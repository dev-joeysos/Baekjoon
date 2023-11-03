def solution(strArr):
    answer = []
    for a in strArr:
        if "ad" in a:
            continue
        else:
            answer.append(a)
    return answer