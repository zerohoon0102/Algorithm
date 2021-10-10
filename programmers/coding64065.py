def solution(s):
    total_arr = []
    tmp = []
    arr = s[1:len(s) - 1]
    n = 0
    while n < len(arr):
        if arr[n] == ',':
            n += 1
        elif arr[n] == '{':
            tmp = []
            n +=1
        elif arr[n] == '}':
            if len(total_arr) == 0:
                total_arr.append(tmp)
            else:
                for m in range(len(total_arr)):
                    if len(total_arr[m]) > len(tmp):
                        total_arr.insert(m, tmp)
                        break
                    else:
                        if m == len(total_arr) - 1:
                            total_arr.append(tmp)
            n += 1
        else:
            length = 1
            tmp_str = arr[n]
            while arr[n+length] != '}' and arr[n+length] != ',':
                tmp_str += arr[n+length]
                length += 1
            n += length
            tmp.append(int(tmp_str))
    answer = []
    for n in range(0, len(total_arr)):
        for m in range(len(answer)):
            total_arr[n].remove(answer[m])
        answer.append(total_arr[n][0])
    return answer