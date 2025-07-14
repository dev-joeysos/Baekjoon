# dac, python 실전에서는 (a**b)%mod 연산에서는 pow(a,b,mod) 활용
import sys
input=sys.stdin.readline

# pow(a,b,mod) 연산의 직접 구현. 여기서 분할정복이 사용
def mod_pow(a,b,mod):
    result=1
    a%=mod
    while b>0:
        if b%2==1:
            result=(result*a)%mod
        a=(a*a)%mod
        b//=2
    return result

def mod_cal(n,s,mod):
    b=mod_pow(n,mod-2,mod)
    a=s
    return (a*b)%mod

def main():
    m=int(input().strip())
    mod=10**9+7
    result=0
    for _ in range(m):
        n,s=map(int,input().split())
        result=(result+mod_cal(n,s,mod))%mod
    print(result)
    
if __name__=="__main__":
    main()