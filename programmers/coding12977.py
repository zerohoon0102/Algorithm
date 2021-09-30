from itertools import combinations

def chess(che):
    for i in range(2, len(che)):
        if che[i] == True:
            for j in range(i+i, len(che), i):
                che[j] = False

def solution(nums):
    answer = 0
    max_value = sum(sorted(nums, reverse = True)[0:3])
    che = [True]*(max_value+1)
    chess(che)
    for tmp in list(combinations(nums, 3)):
        value = sum(tmp)
        if che[value] == True:
            answer += 1

    return answer