def solution(numbers):
    answer = 0
    nums = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    numbers = numbers.replace("one", "1")
    
    for n in nums:
        numbers = numbers.replace(n, str(nums.index(n)))
    return int(numbers)