A, B = input().split()
A = list(A)
B = list(B)
A.reverse()
B.reverse()
rA = int(''.join(A))
rB = int(''.join(B))

if A > B:
    print(''.join(A))
else:
    print(''.join(B))