def solution(n):
    answer = 0
    for i in range(n):
        # 나머지가 0 = pass
        if n % (i+1) == 0:
            answer += 1
    return answer