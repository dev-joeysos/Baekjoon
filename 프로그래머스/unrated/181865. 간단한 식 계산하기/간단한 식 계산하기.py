def solution(binomial):
    answer = 0
    lst = binomial.split()
    c = lst[1]
    if c == '+':
        ans = int(lst[0]) + int(lst[2])
        return ans
    elif c == '-':
        ans = int(lst[0]) - int(lst[2])
        return ans
    else:
        ans = int(lst[0]) * int(lst[2])
        return ans