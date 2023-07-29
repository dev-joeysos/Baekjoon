x = int(input())
arr = [[0]*100 for _ in range(100)]  # 100x100 크기의 2차원 배열 생성

for _ in range(x):
    loc = list(map(int, input().split()))  # 입력 받은 문자열을 정수 리스트로 변환
    for i in range(loc[0], min(loc[0]+10, 100)):  # 색종이가 놓이는 위치 표시
        for j in range(loc[1], min(loc[1]+10, 100)):
            arr[j][i] = 1  # 해당 위치에 색종이가 놓임을 표시

# 색종이가 놓인 위치 수 (= 색종이의 넓이) 계산
paper_area = sum([sum(row) for row in arr])
print(paper_area)
