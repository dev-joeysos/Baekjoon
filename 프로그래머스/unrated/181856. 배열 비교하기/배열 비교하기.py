def solution(a1, a2):
    answer = 0
    if len(a1) != len(a2):
        if len(a1) > len(a2):
            return 1
        else:
            return -1
    else:
        if sum(a1) > sum(a2):
            return 1
        elif sum(a1) < sum(a2): 
            return -1
        else:
            return 0