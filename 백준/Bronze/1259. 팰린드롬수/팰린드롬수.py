import sys
input = sys.stdin.readline


def is_pd(arr, left, right):
    while left < right:
        if arr[left] != arr[right]:
            return False
        left += 1
        right -= 1
    return True


while True:
    A = list(map(int, input().rstrip()))
    if A[0] == 0 and len(A) == 1:
        break
    left, right = 0, len(A)-1
    if is_pd(A, left, right):
        print('yes')
    else:
        print('no')
