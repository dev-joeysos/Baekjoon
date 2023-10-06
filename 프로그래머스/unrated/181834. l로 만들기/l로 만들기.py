def solution(s):
    return ''.join('l' if ord(i)<ord('l') else i for i in s )

# 파이썬 문자열 간의 단순 비교도 지원하기는 함