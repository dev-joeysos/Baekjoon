from itertools import permutations

def solution(k, dungeons):
    answer = -1
    # 던전의 개수가 8개 뿐이고 방문가능한 모든 경로는 8! = 40320 이므로 완전탐색 가능
    max_cnt = 0
    for p in permutations(dungeons, len(dungeons)):
        # 모든 경로에 대해서 조건을 적용해서 최대 방문 횟수를 출력한다.
        cnt = 0
        K = k # k도 모든 경로를 돌 때마다 새로 갱신해줘야 합니다.
        for f in p:
            min_f = f[0]
            exp_f = f[1]
            if K >= min_f: # 최소 피로도 이상이어야 던전 진입합니다.
                K -= exp_f
                cnt += 1
        max_cnt = max(cnt, max_cnt)
    return max_cnt