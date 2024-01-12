def solution(array):
    answer = 0
    array.sort()
    idx = (len(array)-1)//2
    answer = array[idx]
    return answer