def solution(numbers):
    m = max(numbers)
    numbers.remove(m)
    n = max(numbers)
    answer = m*n
    return answer