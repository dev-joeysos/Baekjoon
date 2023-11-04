def solution(n_list):
    cnt=0
    for n in n_list:
        while(True):
            if n == 1:
                break
            else:
                cnt+=1
            if n%2==0:
                n/=2
            else:
                n=(n-1)/2
    return cnt