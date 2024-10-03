# 제거하면서 제거하는 0 개수 세기
def binMachine(s):
    count = s.count('0')
    n = len(''.join(s.split('0')))
    bin_letter = '' 
      
    while n != 0:
        remain = n % 2
        bin_letter = f'{remain}' + bin_letter
        n //= 2

    return count, bin_letter # 바꾼 0 개수, 변환된 이진수
    
def solution(s):
    answer = []
    step = 0
    total = 0
    
    while True:
        step += 1
        count, s = binMachine(s)
        total += count
        if s == '1':
            answer.append(step)
            answer.append(total)
            break
        
    return answer