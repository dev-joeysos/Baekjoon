# dp,LIS,LDS
import sys
input=sys.stdin.readline

def find_LIS(seq,n):
    LIS=[1]*n

    for i in range(n):
        for j in range(i):
            if seq[j]<seq[i]:
                LIS[i]=max(LIS[i],LIS[j]+1)
                
    return LIS

def main():
    n=int(input())
    seq=list(map(int,input().split()))

    LIS=find_LIS(seq,n)
    LDS=find_LIS(seq[::-1],n)[::-1]

    result=0
    for i in range(n):
        length=LIS[i]+LDS[i]-1
        result=max(result,length)
    print(result)
    
if __name__=="__main__":
    main()