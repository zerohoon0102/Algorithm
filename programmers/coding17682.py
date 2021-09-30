def solution(dartResult):
    answer = 0
    point = [0, 0, 0]
    j = -1
    order = 0
    i = 0
    while i < len(dartResult):
        if order == 1 :
            order = 2
            if dartResult[i] == 'D':
                point[j] = point[j] ** 2
            elif dartResult[i] == 'T':
                point[j] = point[j] ** 3
        elif order == 2:
            order = 0
            if dartResult[i] == '*':
                if j == 0 :
                    point[0] = point[0] * 2
                elif j > 0:
                    point[j - 1] = point[j - 1] * 2
                    point[j] = point[j] * 2
            elif dartResult[i] == '#':
                point[j] = -point[j]
            else :
                order = 1
                j = j+1
                if int(dartResult[i]) == 1 :
                    if dartResult[i + 1] == 'S' or dartResult[i + 1] == 'D' or dartResult[i + 1] == 'T':
                        point[j] = 1
                    else:
                        point[j] = 10
                        i = i + 1
                else : 
                    point[j] = int(dartResult[i])
        elif order == 0 :
            order = 1
            j = j+1
            if int(dartResult[i]) == 1 :
                    if dartResult[i + 1] == 'S' or dartResult[i + 1] == 'D' or dartResult[i + 1] == 'T':
                        point[j] = 1
                    else:
                        point[j] = 10
                        i = i + 1
            else:
                point[j] = int(dartResult[i])
        i = i + 1
    
    answer = point[0] + point[1] + point[2]
    return answer