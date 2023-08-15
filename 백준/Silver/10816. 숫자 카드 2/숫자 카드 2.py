N = int(input())
N_lst = list(map(int, input().split()))
M = int(input())
M_lst = list(map(int, input().split()))

# 키: M_lst에 있는 숫자, 값: 그 숫자가 M_lst에 나타나는 횟수
count_dict = {num: 0 for num in M_lst}

# N_lst에 있는 숫자를 세기
for num in N_lst:
    if num in count_dict:
        count_dict[num] += 1

# 결과 출력
count = [count_dict[num] for num in M_lst]
print(' '.join(map(str, count)))
