N = int(input())
if N == 0:  # except
    print(1)
    quit()
sum = 1
while True:
    if N == 0:
        break
    sum *= N
    N -= 1
print(sum)
