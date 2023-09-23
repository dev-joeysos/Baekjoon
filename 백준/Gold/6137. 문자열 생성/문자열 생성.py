import sys
input = sys.stdin.readline


def build_string(s):
    l, r = 0, len(s) - 1  # 출발값
    T = []

    while l <= r:  # 좌우 값이 다를 때

        if s[l] != s[r]:
            if s[l] < s[r]:  # 파이썬은 문자열 간의 비교도 가능하다
                T.append(s[l])
                l += 1
            else:
                T.append(s[r])
                r -= 1

        else:
            temp_l, temp_r = l, r
            while temp_l < temp_r and s[temp_l] == s[temp_r]:  # 다를 때까지 찾기
                temp_l += 1
                temp_r -= 1

            if temp_l >= temp_r or s[temp_l] < s[temp_r]:
                T.append(s[l])
                l += 1
            else:
                T.append(s[r])
                r -= 1
    return ''.join(T)


n = int(input())
s = [input().strip() for _ in range(n)]
s = ''.join(s)
result = build_string(s)
# 출력하기 (80글자마다 줄 바꿈)
for i in range(0, len(result), 80):
    print(''.join(result[i:i+80]))

