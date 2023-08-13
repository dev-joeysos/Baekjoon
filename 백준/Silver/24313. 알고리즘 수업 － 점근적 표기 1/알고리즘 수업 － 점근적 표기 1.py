a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())

def check_O_notation(a1, a0, c, n0):
    # 시작값 n0부터 큰 값까지(예를 들어 1000까지) f(n)과 c×n을 비교합니다.
    for n in range(n0, 1001): 
        if a1 * n + a0 > c * n: # f(n) > c × n 조건을 확인
            return 0 # O(n) 정의를 만족하지 않는 경우
    return 1 # 모든 조건을 통과하면 O(n) 정의를 만족

print(check_O_notation(a1, a0, c, n0))
