def solution(numlist, n):
    answer = []
    for i in sorted(numlist, key=lambda x:[abs(n-x), -x]):
        answer.append(i)
    return answer