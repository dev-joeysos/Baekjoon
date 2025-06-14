#mod연산/재귀/DAC
import sys
input=sys.stdin.readline
a,b,c=map(int,input().split())

def dac(a,b):
    if b==1: #종료조건
        return a%c
    half=dac(a,b//2)
    if b%2==0: #짝수
        return (half*half)%c
    else: #홀수
        return (a*half*half)%c

print(dac(a,b))