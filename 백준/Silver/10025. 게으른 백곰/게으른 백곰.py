N, K = map(int, input().split())
ice = [0] * 1000001  # 아이스크림의 위치가 0부터 1000000까지 가능하므로

# 입력받은 아이스크림 정보를 바탕으로 위치에 따른 양을 저장
for _ in range(N):
    g, x = map(int, input().split())
    ice[x] += g

# 슬라이딩 윈도우 초기 설정
window_sum = sum(ice[:2*K+1])  # 처음 윈도우의 아이스크림 총량
max_sum = window_sum  # 최대 아이스크림 양을 저장할 변수

# 슬라이딩 윈도우를 이동시키며 최대 아이스크림 양 갱신
for i in range(1, 1000001 - 2*K):
    window_sum = window_sum - ice[i-1] + ice[i + 2*K]  # 윈도우 이동
    max_sum = max(max_sum, window_sum)  # 최대값 갱신

print(max_sum)
