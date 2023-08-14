import sys
N = int(input())
arr = list(map(int, sys.stdin.readline().split()))
new_arr = sorted(list(set(arr)))  # 중복이 제거하고 정렬까지 하면 인덱스만 알면 됨

# dictionary comprehension
dict = {}
for idx, num in enumerate(new_arr):
    dict[num] = idx

result = [dict[num] for num in arr]

print(' '.join(map(str, result)))
