def solution(n):
    answer = []
    arr = [i for i in range(1, int((n*(n+1))/2) + 1)]
    arr = sorted(arr, reverse=True)
    result = [[0]*(i+1) for i in range(n)]
    i = 0
    j = 0
    state = 1
    result[0][0] = arr.pop()
    while(len(arr) > 0):
        if state == 1:
            if (i < n-1) and (result[i+1][j] == 0):
                i += 1
                result[i][j] = arr.pop()
            else:
                state = 2
        elif state == 2:
            if (j < len(result[i]) - 1) and (result[i][j+1] == 0):
                j += 1
                result[i][j] = arr.pop()
            else:
                state = 3
        elif state == 3:
            if (i >= 0 ) and (result[i-1][j-1] == 0):
                i -= 1
                j -= 1
                result[i][j] = arr.pop()
            else:
                state = 1
    for q in result:
        answer += q
    return answer