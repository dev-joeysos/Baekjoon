'''
최장길이 공통수열
Longest Common Subsequence
'''
import sys
input=sys.stdin.readline

def find_max_value(a,b,a_start_idx,b_start_idx):
    max_val=-1
    for a_num in a[a_start_idx:]:
        for b_num in b[b_start_idx:]:
            if a_num==b_num:
                if a_num>max_val:
                    max_val=a_num
                break
    return max_val if max_val!=-1 else False

def find_max_common_subsequence(a,b):
    a_start_idx=0
    b_start_idx=0
    answer=[]
    while True:
        max_common_value=find_max_value(a,b,a_start_idx,b_start_idx)
        if not max_common_value:
            break
        answer.append(max_common_value)
        a_start_idx=a.index(max_common_value,a_start_idx)+1
        b_start_idx=b.index(max_common_value,b_start_idx)+1
    
    return answer

def main():
    n=int(input().strip())
    a=list(map(int,input().split()))
    m=int(input().strip())
    b=list(map(int,input().split()))
    
    answer=find_max_common_subsequence(a,b)
    print(len(answer))
    print(' '.join(map(str,answer)))
    
if __name__=="__main__":
    main()