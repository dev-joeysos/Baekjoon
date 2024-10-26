n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

def solution(n, A, B):
    S = 0
    sortedA = sorted(A)
    sortedB = sorted(B, reverse=True)
    for i in range(n):
        S += sortedA[i] * sortedB[i]
        
    return S

print(solution(n, A, B))