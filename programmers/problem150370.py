def solution(today, terms, privacies):
    answer = []
    menu = {}
    for term in terms:
        term_type, term_range = term.split()
        menu[term_type] = int(term_range)
    
    today_year, today_month, today_day = map(int, today.split('.'))
    for idx, privacy in enumerate(privacies):
        date, term_type = privacy.split()
        year, month, day = map(int, date.split('.'))
        year += (month+menu[term_type]-1)//12
        month = (month+menu[term_type]-1)%12 + 1
        if today_year > year or (today_year == year and (today_month > month or (today_month == month and today_day >= day))):
            answer.append(idx+1)
        
    return answer
