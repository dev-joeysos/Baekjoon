def solution(arr, ver):
    ans = []
    
    for a,b in ver:
        ans += arr[a:b+1]
    
    return ans