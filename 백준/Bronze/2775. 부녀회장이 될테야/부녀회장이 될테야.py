# 1일 1백준
# DP 연습
# 부녀회장이 될테야
'''
재귀 dp = 시간초과
'''
T=int(input())

for i in range(T):
    k=int(input())
    n=int(input())
    people = [i for i in range(1,n+1)]

    for x in range(k):
        for y in range(1, n):
            people[y] += people[y-1]
    print(people[-1])

