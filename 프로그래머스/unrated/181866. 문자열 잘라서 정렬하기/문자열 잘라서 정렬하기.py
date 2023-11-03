def solution(S):
    return sorted([s for s in S.split("x") if len(s) != 0])
