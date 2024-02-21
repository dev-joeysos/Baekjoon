N = int(input())
start = 1
end = 1
i = 1
while True:
    if N in range(start, end+1):
        print(i)
        break
    start = end + 1
    end += 6*i
    i += 1