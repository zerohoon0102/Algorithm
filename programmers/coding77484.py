def solution(lottos, win_nums):
    answer = []
    zero = 0
    know = 0
    for lotto in lottos:
        if lotto == 0:
            zero += 1
        elif lotto in win_nums:
            know += 1
    if (know + zero) > 1:
        answer.append(7 - know - zero)
    else:
        answer.append(6)
    if (know == 1) or (know == 0):
        answer.append(6)
    else:
        answer.append(7 - know)
    return answer