'''
집합과 맵
'''

N = int(input())
answer = list(map(int, input().split()))

M = int(input())
quest = list(map(int, input().split()))

dict = {}
for num in answer:
    dict[num] = 1

result = []
for x in quest:
    if x in dict:
        result.append(1)
    else:
        result.append(0)

print(' '.join(map(str, result)))
