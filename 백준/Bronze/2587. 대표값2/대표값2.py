# 대표값2

# 정렬하고 가장 중앙에 놓인 값

arr = [int(input()) for _ in range(5)]
arr.sort()
average = 0
for num in arr:
    average += num

average /= 5
print(int(average))
print(arr[2])
