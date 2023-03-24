N = input() #input()는 입력값을 문자열로 반환한다.
if N == N[::-1]: #문자열과 문자열을 뒤집은 결과가 같은지 여부를 확인한다.
    print("1")
else:
    print("0")
