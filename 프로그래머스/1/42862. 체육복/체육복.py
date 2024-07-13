def solution(n, lost, reserve):
    # 여벌이 있는데 도난당한 경우를 처리합니다.
    lost_only = [l for l in lost if l not in reserve]
    reserve_only = [r for r in reserve if r not in lost]
    
    # 여벌 체육복을 빌려줍니다.
    for los in sorted(lost_only):
        if los - 1 in reserve_only:
            reserve_only.remove(los - 1)
        elif los + 1 in reserve_only:
            reserve_only.remove(los + 1)
        else:
            n -= 1
    
    return n
