S = input()
new_S = set()
for i in range(1, len(S) + 1):
    for j in range(len(S) - i + 1):
        new_S.add(S[j:j+i])

print(len(new_S))
