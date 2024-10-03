def toDictionary(terms):
    term_dict = {}
    for term in terms:
        type, month = term.split()
        term_dict[type] = month
    return term_dict

def solution(today, terms, privacies):
    answer = []
    term_dict = toDictionary(terms)
    today_year, today_month, today_day = map(int, today.split('.'))
    
    for idx, privacy in enumerate(privacies):
        date, type = privacy.split()
        year, month, day = map(int, date.split('.'))

        term_month = int(term_dict[type])
        month += term_month

        # 연도 및 월 계산
        year += (month - 1) // 12
        month = (month - 1) % 12 + 1

        # 날짜 비교
        if year < today_year or (year == today_year and (month < today_month or (month == today_month and day <= today_day))):
            answer.append(idx + 1)
    
    return answer
