import sys
input = sys.stdin.readline

def is_pd(s, left, right):
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

t = int(input())

for _ in range(t):
    s = list(input().rstrip())
    left, right = 0, len(s) - 1

    while left < right:
        if s[left] != s[right]:
            # 한 문자를 제거하여 펠린드롬을 만드는지 확인
            if is_pd(s, left + 1, right) or is_pd(s, left, right - 1):
                print(1)
            else:
                print(2)
            break
        left += 1
        right -= 1
    else:  # 정상적으로 펠린드롬을 찾으면
        print(0)
