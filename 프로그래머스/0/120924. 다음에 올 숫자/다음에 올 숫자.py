def solution(c):
    if c[1] - c[0] == c[2] - c[1]:
        return c[-1] + (c[1] - c[0])
    else:
        val = c[1] / c[0]
        return c[-1] * val
        