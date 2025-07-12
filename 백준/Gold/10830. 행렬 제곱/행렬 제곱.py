'''
행렬제곱
'''
import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

# 행렬 곱셈
def mat_mul(A, B):
    n=len(A)
    result=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j]+=A[i][k]*B[k][j]
            result[i][j]%=1000
    return result

def mat_pow(matrix,b):
    # base case
    if b==1:
        return [[x%1000 for x in row] for row in matrix]
    
    half=mat_pow(matrix,b//2)
    result=mat_mul(half,half)
    
    # 홀수 제곱일 경우 한 번 더 곱해줌
    if b%2==1:
        result=mat_mul(result,matrix)
    
    return result

def main():
   n,b=map(int,input().split())
   matrix=[list(map(int,input().split())) for _ in range(n)]
   result=mat_pow(matrix,b)
   for row in result:
       print(*row)
    
if __name__=="__main__":
    main()