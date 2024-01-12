def solution(array):
    answer = 0
    
    m = 0
    lst = list(set(array)) # [1 2 3 4] 
    check = [0 for i in range(len(lst))] # [1 1 3 1]
    
    for i in range(len(lst)):
        tmp = array.count(lst[i])
        check[i] += tmp
        
    m = max(check)
    cnt = 0
    for c in check:
        if c == m:
            cnt += 1
        if cnt > 1:
            return -1
    else:
        tmp = check.index(m)
        return lst[tmp]