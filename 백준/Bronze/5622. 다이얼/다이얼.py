word = list(input())
lst = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
time = 0
for i in range(len(word)):
    for j in range(len(lst)):
        if word[i] in lst[j]:
            time = time + (j+3)  # 0부터 시작해서 (+1) + 알파벳에 해당하는 번호 + 2초만큼 시간이 추가
print(time)