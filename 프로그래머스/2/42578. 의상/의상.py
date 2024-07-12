'''
가능한 모든 옷의 조합 수 출력
딕셔너리 익숙해지기
'''
def solution(clothes):
    dic = {}
    for name, kind in clothes:
        if kind in dic:
            dic[kind] += [name] 
        else:
            dic[kind] = [name]
    answer = 1
    for _, val in dic.items():
        answer *= (len(val) + 1)
    return answer - 1