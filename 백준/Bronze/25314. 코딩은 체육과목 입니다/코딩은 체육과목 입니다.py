N = int(input())
if N % 4 == 0:
    # 배열에 속하는 원소를 직접 연산해서 배열에 삽입할 수 있다.
    l_array = ["long "] * (N // 4) + ["int"]
    print(''.join(l_array))
else:
    print("N은 4의 배수가 아닙니다.")
