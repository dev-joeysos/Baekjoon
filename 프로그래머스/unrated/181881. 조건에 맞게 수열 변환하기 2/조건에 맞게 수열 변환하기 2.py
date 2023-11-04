def solution(arr):
    x= 0
    while(True):
        check = []
        for a in arr:
            if a >= 50 and a % 2 == 0:
                a /= 2
            elif a < 50 and a % 2 == 1:
                a = a * 2 + 1
            check.append(a)
    
        if check == arr:
            break
        else:
            arr = check # update new arr
            x += 1
    return x