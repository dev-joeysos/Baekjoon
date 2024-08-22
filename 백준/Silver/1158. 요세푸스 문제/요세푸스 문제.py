def josephus(N, K):
    people = list(range(1, N+1))  # 1부터 N까지의 사람 리스트 생성
    answer = []
    index = 0

    while people:
        index = (index + K - 1) % len(people)
        answer.append(people.pop(index))

    return answer

N, K = map(int, input().split())
result = josephus(N, K)
print('<', end='')
print(', '.join(map(str, result)), end='')
print('>')