def solution(answers):
    answer = []
    f_arr = [1,2,3,4,5]
    s_arr = [2,1,2,3,2,4,2,5]
    t_arr = [3,3,1,1,2,2,4,4,5,5]
    f = 0
    s = 0
    t = 0
    for i in range(len(answers)):
        ans = answers[i]
        if f_arr[i%5] == ans:
            f += 1
        if s_arr[i%8] == ans:
            s += 1
        if t_arr[i%10] == ans:
            t += 1
    m = max(f,max(s,t))
    if f == m:
        answer.append(1)
    if s == m:
        answer.append(2)
    if t ==m:
        answer.append(3)
    return answer