def solution(arr, k):
    ans=[]
    for i in arr:
        if i not in ans:
            ans.append(i)
    while len(ans) < k:
        ans.append(-1)
    return ans[:k]