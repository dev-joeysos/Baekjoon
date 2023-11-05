def solution(n):
    ans = []
    for i in str(n):
        ans.append(int(i))
    rst = []
    for _ in range(len(ans)):
        tmp = ans.pop()
        rst.append(tmp)
    return rst