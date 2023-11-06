def solution(numbers):
    answer = -1
    lst = [x for x in range(10)]
    
    for n in numbers:
        lst.remove(n)
    return sum(lst)