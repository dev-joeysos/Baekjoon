def solution(arr):
    answer = []
    for a in arr:
        if a >= 50 and a%2==0:
            a /= 2
            answer.append(a)
        elif a<50 and a%2:
            a *= 2
            answer.append(a)
        else:
            answer.append(a)
    return answer