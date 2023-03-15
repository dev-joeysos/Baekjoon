T = int(input())
t = []
for i in range(T):
    s = input()
    if len(s) == 1:
        t.append(s[0] + s[0])
    else:
        t.append(s[0] + s[-1])
print(*t, sep='\n')