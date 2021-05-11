def solution(rows, columns, queries):
    answer = []
    square = [[columns*i + j for j in range(1, columns + 1)] for i in range(0, rows)]
    for query in queries:
        top, left, bot, right = query[0]-1, query[1]-1,query[2]-1,query[3]-1
        x = left
        y = top
        bef = square[top+1][left]
        tmp_min = bef
        while( 1 ):
            cur = square[y][x]
            square[y][x] = bef
            bef = cur
            tmp_min = min(tmp_min, bef)
            if ((x < right) and (y == top)):
                x += 1
            elif ((x == right) and (y < bot)):
                y += 1
            elif ((x > left) and (y == bot)):
                x -= 1
            elif ((x == left) and (y > top)):
                y -= 1
            if ((x == left) and (y == top)):
                break
        answer.append(tmp_min)
    return answer