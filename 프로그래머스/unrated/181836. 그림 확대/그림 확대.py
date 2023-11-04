def solution(P, k):
    answer = []
    for p in P: # ".xx...xx."
        TMP = ''
        for x in p:
            for _ in range(k):
                TMP += x
        # print(TMP)
        for _ in range(k):
            answer.append(TMP)
    return answer