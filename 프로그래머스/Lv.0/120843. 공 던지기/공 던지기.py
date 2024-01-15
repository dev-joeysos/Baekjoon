def solution(numbers, k):
    if 2*(k-1) >= len(numbers):
        return numbers[2*(k-1) % len(numbers)]
    else:
        return numbers[2*(k-1)]
