# 1. 생성자를 통해 만들어지는 수들 기록
# 2. 전체 수 중, 위에서 기록 안 된 수들만 출력

# d(n) = n + 각 자리수 합
def d(n):
    return n + sum(map(int, str(n)))

# 1부터 10000까지 생성된 수 기록
generated = set()
for i in range(1, 10001):
    generated.add(d(i))

# 1부터 10000까지 중 생성되지 않은 수 출력
for i in range(1, 10001):
    if i not in generated:
        print(i)
