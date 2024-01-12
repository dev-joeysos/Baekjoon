def solution(ms, lt):
    ans = ''
    for m in ms:
        if m != lt:
            ans+=m
    return ans