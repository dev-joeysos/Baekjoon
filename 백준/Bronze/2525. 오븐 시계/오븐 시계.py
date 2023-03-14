A, B = map(int, input().split())
C = int(input())
a = C//60
b = C % 60
B = B + b
if 59 < B:  # 60분을 넘어가면
    ta = B//60  # 시간
    B = B % 60  # 분

    a = a + ta  # 더해주는 조리 시간

A = A + a
if 23 < A:
    A = A % 24  # 출력해야 하는게 결국 끝나는 시간

print(A, B)