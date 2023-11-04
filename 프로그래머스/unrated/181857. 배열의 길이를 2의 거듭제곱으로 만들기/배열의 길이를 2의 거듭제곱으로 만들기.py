def solution(arr):
    i=-1
    l=len(arr)
    while(True):
        if 2**i < l and l<=2**(i+1):
            cnt = 2**(i+1)
            break
        else:
            i+=1

    for _ in range(cnt-l):
        arr.append(0)
    return arr