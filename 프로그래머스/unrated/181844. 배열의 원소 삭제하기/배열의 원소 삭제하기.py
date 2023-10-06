def solution(arr, dl):
    answer = []
    for a in arr:
        if a not in dl:
            answer.append(a)
    return answer