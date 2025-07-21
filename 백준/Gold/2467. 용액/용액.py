'''
투포인터 이진탐색
'''
import sys
input=sys.stdin.readline

def two_pointer(lst):
    INF=float("inf")
    result=INF
    start,end=0,len(lst)-1
    answer=(0,0)
    while (start<end):
        total=lst[start]+lst[end]
        if abs(total)<result:
            result=abs(total)
            answer=(lst[start],lst[end])
        if total<0:
            start+=1
        else:
            end-=1
    return answer

def main():
    n=int(input())
    values=list(map(int,input().split()))
    values.sort()
    print(*two_pointer(values))
    
if __name__=="__main__":
    main()