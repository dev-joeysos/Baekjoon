def gcd(a, b): 
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def solution(arr):
    temp = 1
    for i in range(len(arr)):
        temp = lcm(temp, arr[i])
    return temp