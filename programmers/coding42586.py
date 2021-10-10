def solution(progresses, speeds):
    answer = []
    start = 0
    length = len(progresses)
    while(start < length):
        chk = 0
        for i in range(start, length):
            progresses[i] += speeds[i]
        for j in range(start, length):
            if progresses[j] >= 100:
                start += 1
                chk += 1
            else:
                break
        if chk > 0:
            answer.append(chk)
    return answer