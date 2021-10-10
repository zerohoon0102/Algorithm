def solution(s):
    answer = len(s)
    full_answer = answer
    half_answer = 0
    if(full_answer % 2 == 1):
        half_answer = int((full_answer - 1) / 2 )
    else:
        half_answer = int(full_answer / 2)
    total = 1
    comp_ans = 0
    comp = 0
    for a in range(1, half_answer + 1):
        comp_ans = full_answer
        comp = 0
        while comp < full_answer:
            if comp+a+a > full_answer:
                if total != 1:
                    last = 1
                    last_total = total
                    while last_total >= 10:
                        last_total = last_total/10
                        last = last + 1
                    comp_ans = comp_ans - (total - 1) * a + last
                    total = 1
                    break;
            else:
                if s[comp:comp+a] == s[comp+a:comp+a+a]:
                    total = total + 1
                else:
                    if total != 1:
                        last = 1
                        last_total = total
                        while last_total >= 10:
                            last_total = last_total/10
                            last = last + 1
                        comp_ans = comp_ans - (total - 1) * a + last
                        total = 1
            comp = comp + a
        if answer > comp_ans:
            answer = comp_ans

    return answer