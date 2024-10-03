# great common divisor
def gcd(a, b): 
    val = 1
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            val = i
    return val

# least common multiplier
def lcm(a, b):
    return a * b // gcd(a, b)

def solution(arr):
    temp = 1
    
    for i in range(len(arr)):
        temp = lcm(temp, arr[i])
        print(f'temp = {temp}')
    return temp

print(solution([2,6,8,14]))