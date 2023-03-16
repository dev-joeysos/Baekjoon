import string
S = list(input())
al = list(string.ascii_lowercase)

for i in range(len(S)):
    for j in range(len(al)):
        if S[i] == al[j]:
            al[j] = i

for i in range(len(al)):
    if not str(al[i]).isdigit():
        al[i] = -1
print(*al)