n = int(input())
count = n  # 그룹 단어의 개수

for _ in range(n):
    word = input()
    for i in range(len(word)-1):
        if word[i] != word[i+1]:
            if word[i] in word[i+1:]:  # 현재 문자가 이후에 또 등장한다면
                count -= 1  # 그룹 단어가 아님
                break  # 반복 중단
print(count)