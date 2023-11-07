def solution(n, m):
    answer = []
    
    def gcd(a,b):
        while(b):
            a,b = b,a%b
        return a
    
    def lcm(a,b):
        result = (a*b)//gcd(a,b)
        return result

    return [gcd(n,m), lcm(n,m)]