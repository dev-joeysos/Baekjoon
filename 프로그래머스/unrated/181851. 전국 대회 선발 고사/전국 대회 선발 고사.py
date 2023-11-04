def solution(rnk, ad):
    ans = 0
    arr = []
    cnt = 0
    
    rst = []
    for i in range(len(rnk)):
        arr.append([rnk[i], ad[i], cnt])
        cnt += 1
    arr.sort()
    # print(arr)
    
    for item in arr:
        if item[1]:
            rst.append(item[2])
    # print(rst)
    ans = rst[0]*10000 + rst[1]*100 + rst[2]
    return ans