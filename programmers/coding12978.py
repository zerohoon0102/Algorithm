def solution(N, roads, K):
    answer = 0
    INF = 500001
    info = [[INF]*N for _ in range(N)]
    for road in roads:
        a, b, time = road
        a -= 1
        b -= 1
        if time < info[a][b]:
            info[a][b] = time
            info[b][a] = time
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            for k in range(N):
                if j == k:
                    info[j][k] = 0
                    continue
                if (info[j][i] + info[i][k]) < info[j][k]:
                    info[j][k] = info[j][i] + info[i][k]
    for i in range(N):
        if info[0][i] <= K:
            answer += 1
    return answer