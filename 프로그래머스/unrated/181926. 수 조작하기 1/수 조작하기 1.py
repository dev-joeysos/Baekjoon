def solution(n, control):
    c={'w':1, 's':-1, 'd':10, 'a':-10}
    for key in control:
        n += c[key]
    return n