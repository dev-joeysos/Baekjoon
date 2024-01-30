def solution(p):
    answer = ''
    X,A = 0,0
    p_lst = list(p.split(' + '))

    for item in p_lst:
        if item.isdigit():
            A += int(item)

        else:
            if item == 'x':
                X += 1
            else:
                X += int(item[:-1])
            
    if X == 0:
        return str(A)
    elif X == 1:
        return 'x' + (' + ' + str(A) if A!=0 else '') 
    elif A == 0:
        return str(X) + 'x'
    else:
        return str(X) + 'x + ' + str(A)
        
    return answer