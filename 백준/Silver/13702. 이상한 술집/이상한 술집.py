# 1일 1백준
# 이상한 술집 _ 이진탐색, 매개변수 탐색
n,k = map(int,input().split())
lst = []
for i in range(n):
   lst.append(int(input()))

start = 1
end = max(lst)
res = 0

while(start<=end):
   tmp = 0
   mid = ( start + end ) // 2
   for item in lst:
      tmp += item//mid
   if tmp >= k:
      res = mid
      start = mid + 1
   else:
      end = mid - 1
print(res)
