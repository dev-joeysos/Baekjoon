# union_find
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num_truth, *truth_people = map(int, input().split())

parties = []
for _ in range(m):
    _, *party_members = map(int, input().split())
    parties.append(party_members)

# 유니온 파인드 셋업
parent = [i for i in range(n + 1)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x_root = find(x)
    y_root = find(y)
    if x_root != y_root:
        parent[y_root] = x_root

# 진실 아는 사람 여러 명이면 같은 그룹으로 미리 묶기
if truth_people:
    base = truth_people[0]
    for person in truth_people[1:]:
        union(base, person)

# 파티별로 참석자들끼리 묶기
for party in parties:
    first = party[0]
    for person in party[1:]:
        union(first, person)

# 진실을 아는 그룹 루트
truth_roots = [find(person) for person in truth_people]

result = 0
for party in parties:
    # 파티원 중에 진실 그룹 루트와 같은 사람이 있으면 거짓말 불가
    if any(find(person) in truth_roots for person in party):
        continue
    result += 1

print(result)
