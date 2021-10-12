def solution(msg):
    answer = []
    A2Z = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    dic = [t for t in A2Z]
    n = 0
    while n < len(msg):
        tmp = msg[n]
        while (n < len(msg) - 1) and ((tmp + msg[n+1]) in dic):
            n += 1
            tmp += msg[n]
        answer.append(dic.index(tmp) + 1)
        if n < len(msg) - 1:
            dic.append(tmp + msg[n+1])
        n += 1
    return answer