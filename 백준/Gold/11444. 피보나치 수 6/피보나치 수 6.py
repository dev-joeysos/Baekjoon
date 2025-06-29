import sys
input=sys.stdin.readline
n=int(input().strip())

MOD=10**9+7

# 2*2 행렬 곱셈 연산
def mat_mul(A,B):
    result=[[0,0],[0,0]]
    for i in range(2): # 행
        for j in range(2): # 열
            for k in range(2): # 축
                result[i][j]=(result[i][j]+A[i][k]*B[k][j])%MOD
    return result

# 행렬 연산임을 잊지말것!  
def fast_pow(mat,exp):
    # mat=기본행렬
    # exp=거듭제곱의 지수
    if exp==0:
        return [[1,0],[0,1]] # 2X2 지수가 0일 때의 단위 행렬
    if exp==1:
        return mat
    
    if exp%2==0: #짝수
        half=fast_pow(mat,exp//2)
        return mat_mul(half,half)
    else: #홀수
        half=fast_pow(mat,exp-1)
        return mat_mul(half,mat)

base=[[1,1],[1,0]]
result=fast_pow(base,n-1)

vector=[1,0]

answer=[0,0]
for i in range(2):
    for j in range(2):
        answer[i]+=result[i][j]*vector[j]
        answer[i]%=MOD

print(answer[0])