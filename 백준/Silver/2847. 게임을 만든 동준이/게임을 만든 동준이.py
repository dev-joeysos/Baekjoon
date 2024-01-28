'''
아이디어
뒤에서부터 낮춘다.
'''

N=int(input())
lst=[]
for _ in range(N):
    tmp=int(input())
    lst.append(tmp)

cnt = 0
for i in range(len(lst)-1, 0, -1):
    if lst[i] <= lst[i-1]:
        cnt += lst[i-1] - lst[i] + 1
        lst[i-1] = lst[i] - 1
    # print(i, lst)
print(cnt)