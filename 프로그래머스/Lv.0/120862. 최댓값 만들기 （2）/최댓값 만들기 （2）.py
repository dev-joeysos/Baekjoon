def solution(nbs):
    '''
    정렬 후 가장 작은 두 음수, 가장 큰 두 양수를 곱해서 큰 값을 출력
    '''
    nbs.sort()
    return max(nbs[0]*nbs[1], nbs[-1]*nbs[-2])