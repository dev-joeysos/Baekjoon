def solution(arr, flag):
    answer = []
    for i in range(len(flag)):
        if flag[i]:
            tmp = (arr[i])*2
            for _ in range(tmp):
                answer.append(arr[i])
        else:
            for _ in range(arr[i]):
                del answer[-1]
    return answer