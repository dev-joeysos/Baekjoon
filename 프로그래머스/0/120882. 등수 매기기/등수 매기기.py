def solution(score):
    # clean code
    a = sorted([sum(i) for i in score], reverse = True)
    return [a.index(sum(i)) + 1 for i in score]