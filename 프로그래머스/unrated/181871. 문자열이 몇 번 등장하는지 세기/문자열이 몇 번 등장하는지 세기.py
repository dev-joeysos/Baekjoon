def solution(S, pat):
    answer = 0
    l = len(pat)
    for i in range(0,len(S)-l+1):
        if pat == S[i:i+l]:
            answer += 1
    return answer