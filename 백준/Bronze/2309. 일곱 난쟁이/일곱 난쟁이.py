total = 0
sm = [int(input()) for _ in range(9)]
distance = sum(sm) - 100

found = False
for i in range(len(sm)):
    for j in range(i + 1, len(sm)):
        if sm[i] + sm[j] == distance:
            first, second = sm[i], sm[j]
            found = True
            break
    if found:
        break
    
sm.remove(second)
sm.remove(first)
sm.sort()
for s in sm:
    print(s)

# 브루트 포스 이중 반복문 기초 문제