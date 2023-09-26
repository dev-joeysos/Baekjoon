def solution(my_string, alp):
    ans = ''
    for s in my_string:
        if s == alp:
            ans += s.upper()
        else:
            ans += s
    return ans