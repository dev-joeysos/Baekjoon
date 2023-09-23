import sys
input = sys.stdin.readline
n = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))
x = int(input().rstrip())
arr.sort()
cnt = 0
l, r = 0, len(arr)-1
while l < r:
    sum = arr[l]+arr[r]
    if sum > x:  # 합이 작으면
        r -= 1
    elif sum < x:  # 합이 크면
        l += 1
    else:  # 같으면
        cnt += 1
        l += 1
        r -= 1
print(cnt)