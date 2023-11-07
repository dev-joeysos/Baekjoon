def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)): #2 
        T = []
        for j in range(len(arr1[0])): #3
            tmp = arr1[i][j] + arr2[i][j]
            T.append(tmp)
        answer.append(T)
    return answer