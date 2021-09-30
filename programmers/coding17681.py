def solution(n, arr1, arr2):
    answer = []
    temp = ""
    j = n - 1
    for i in range(0, n) :
        while j >= 0 :
            if ((arr1[i] // 2**j) == 0) and ((arr2[i] // 2**j) == 0) :
                temp = temp + ' '
            else :
                temp = temp + '#'
                if (arr1[i] // 2**j) > 0:
                    arr1[i] = arr1[i] - 2**j
                if (arr2[i] // 2**j) > 0:
                    arr2[i] = arr2[i] - 2**j
            j = j-1
        answer.append(temp)
        temp = ""
        j = n - 1
              
    return answer