'''
(제일큰거)*(제일작은거)
'''
T = int(input())
arr = list(map(int, input().split()))
N = max(arr)*min(arr)
print(N)
