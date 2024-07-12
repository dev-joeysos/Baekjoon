'''
한 번호가 다른 번호의 접두어인 경우가 있을까?

전화번호의 어떤 번호가 다른 번호의 접두어인 경우가 있으면 false,
아니면 true를 반환한다

사실 정렬하면 된다...

'''
def solution(phone_book):
    answer = True

    hash_map = {}
    for num in phone_book:
        hash_map[num] = 1
    
    for number in phone_book:
        result = ""
        for num in number:
            result += num
            if result in hash_map and result != number:
                answer = False
                return answer
    return answer
    
    
    return answer