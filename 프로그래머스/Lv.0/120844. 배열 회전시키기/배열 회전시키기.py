def solution(nbs, dir):
    ans = []
    if dir == 'right':
        ans.append(nbs[-1])
        for i in range(len(nbs)-1):
            ans.append(nbs[i])
    else:   
        for i in range(1, len(nbs)):
            ans.append(nbs[i])
        ans.append(nbs[0])
    return ans