# 1 일 1 백준
hurt = int(input())
n = int(input())
finger = [1,2,3,4,5,4,3,2]
rst = 0

if hurt == 1:
    rst = n*8
elif hurt == 2:
    if n%2 != 0: # 홀수
        tmp = n//2
        rst = 1 + 2*tmp + 6*(tmp+1)
    else: # 짝수
        tmp = n//2
        rst = 1 + 2*(tmp) + 6*(tmp)
elif hurt == 3:
    rst = 2 + 4*n
elif hurt == 4:
    if n%2 != 0: # 홀수
        tmp = n//2
        rst = 3 + 6*tmp + 2*(tmp+1)
    else: # 짝수
        tmp = n//2
        rst = 3 + 6*(tmp) + 2*(tmp)
elif hurt == 5:
    rst = 4 + 8*n

print(rst)