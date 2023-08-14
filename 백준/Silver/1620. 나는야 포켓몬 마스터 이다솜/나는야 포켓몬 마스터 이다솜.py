N, M = map(int, input().split())
S = []
Q = []
for _ in range(N):
    x = input()
    S.append(x)

for _ in range(M):
    x = input()
    Q.append(x)

dict = {}
dict2 = {}

for idx, name in enumerate(S):
    dict[name] = idx
    dict2[idx] = name
    # dict = {name: idx}

result = []
for letter in Q:
    # 문자인 경우
    if letter in dict:
        num = dict[letter]
        result.append(num+1)
    # 숫자인 경우
    else:
        check = int(letter) - 1
        name = dict2[check]
        result.append(name)

for i in range(M):
    print(result[i])
