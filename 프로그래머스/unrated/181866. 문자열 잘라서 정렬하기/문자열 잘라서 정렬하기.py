def solution(S):
    ans = []
    tmp = ''
    
    for s in S:
        if s != 'x':
            tmp += s
        else:
            if len(tmp) != 0:
                ans.append(tmp)
                tmp = ''

    if len(tmp) != 0:
        ans.append(tmp)
    
    ans.sort()
    
    return ans