def solution(x):
    answer = True
    lst = list(map(int, str(x)))
    
    if not x % sum(lst):
        return True
    else:
        return False