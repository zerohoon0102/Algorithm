def solution(N, stages):
    answer = []
    user_num = len(stages)
    for i in range(1, N + 1):
        if user_num > 0:
            answer.append(stages.count(i)/user_num)
            user_num = user_num - stages.count(i)
        elif user_num == 0:
            answer.append(0)
    temp = [x for x,y in sorted(enumerate(answer), key = lambda a: a[1], reverse = True)]
    for a in range(0, len(temp)):
        temp[a] = temp[a] + 1
    return temp