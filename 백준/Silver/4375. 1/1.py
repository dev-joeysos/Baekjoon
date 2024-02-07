# 1일 1백준
'''
각 자리가 모두 1로 구성된 n의 배수의 자리수를 출력하는 문제

n의 배수를 구해서 1로 구성됐는지 확인한다 X
1의 배수를 만들어서 n의 배수인지 확인한다 o
'''
import sys

while 1:
    try:
        n = int(sys.stdin.readline())
    except:
        break

    # i는 자리수
    i = 1
    check_num = 1

    while 1:
        if check_num % n == 0:
            print(i)
            break
        check_num = 10*check_num + 1
        i += 1