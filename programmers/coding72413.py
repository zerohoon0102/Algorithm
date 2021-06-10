def solution(n, s, a, b, fares):
    t_max = 2000000000
    info = [0] + [[t_max]*(n+1) for _ in range(n)]
    for fare in fares:
        l, r, v = fare
        info[l][r] = v
        info[r][l] = v
    for i in range(1, n+1):
        info[i][i] = 0
        for j in range(1, n+1):
            if i == j:
                continue
            for k in range(j+1, n+1):
                if k==i:
                    continue
                if (info[j][i] == t_max) or (info[i][k] == t_max):
                    continue
                if (info[j][i] + info[i][k] < info[j][k]):
                    info[j][k] = info[j][i] + info[i][k]
                if (info[k][i] + info[k][j] < info[j][i]):
                    info[k][j] = info[k][i] + info[k][j]
    answer = info[s][a] + info[s][b]
    for i in range(1, n+1):
        if (i == s) or (info[s][i] == t_max) or (info[i][a] == t_max) or (info[i][b] == t_max):
            continue
        answer = min(info[s][i] + info[i][a] + info[i][b], answer)
    return answer