# 수 정렬하기

# 오름차순 정렬

N = int(input())
arr = [int(input()) for _ in range(N)]

# 정렬 함수를 사용하지 않고
# 가장 작은 값을 골라서 1번에 배치
# 배치했으면 인덱스를 늘림
new = []
for _ in range(len(arr)):
    x = min(arr)
    new.append(x)
    arr.remove(x)

for num in new:
    print(num)
