def solution(triangle):
    answer = 0
    for i in range(0, len(triangle)-1):
        prev_S = triangle[i]
        S = triangle[i+1]
        
        for idx, s in enumerate(S):
            if idx == 0:
                s += prev_S[0]
            elif idx == len(S) - 1:
                s += prev_S[-1]
            else:
                s += max(prev_S[idx-1], prev_S[idx])
            S[idx] = s
    
    answer = max(S)
    return answer