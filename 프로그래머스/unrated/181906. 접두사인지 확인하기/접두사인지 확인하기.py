def solution(my_string, is_prefix):
    answer = 0
    if is_prefix in my_string:
        return 1 if my_string[:len(is_prefix)] == is_prefix else 0
    else:
        return 0