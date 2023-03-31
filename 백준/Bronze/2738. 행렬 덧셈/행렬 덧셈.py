N, M = map(int, input().split())
A, B = [], []
#이중 리스트 선언
for row in range(N):
    row = list(map(int, input().split())) 
    A.append(row)
#이중 리스트 선언
for row in range(N):
    row = list(map(int, input().split()))
    B.append(row)
#더한 값 그대로 출력
for row in range(N):
    for col in range(M):
        print(A[row][col] + B[row][col], end=' ')
    print() 