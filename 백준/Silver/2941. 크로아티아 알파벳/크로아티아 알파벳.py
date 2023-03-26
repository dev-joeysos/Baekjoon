s = input()  # 문자열 입력받기
count = 0  # 문자의 개수를 저장할 변수 초기화
new_s = ''  # 문자를 공백으로 대체한 새로운 문자열을 저장할 변수 초기화
croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

i = 0  # 인덱스 변수 초기화
while i < len(s):
    if s[i:i+3] in croatia:
        count += 1
        new_s += '0' * 3  # 대체할 문자열 길이만큼 '0' 추가
        i += 3  # 세 글자를 건너뜀
    elif s[i:i+2] in croatia:
        count += 1
        new_s += '0' * 2  # 대체할 문자열 길이만큼 '0' 추가
        i += 2  # 두 글자를 건너뜀
    else:
        new_s += s[i]
        i += 1

for i in range(len(new_s)):
    if new_s[i] != '0':
        count += 1

print(count)