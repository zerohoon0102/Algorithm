def solution(numbers, hand):
    answer = ''
    left = 10
    right = 12
    for num in numbers:
        if num == 0:
            num = 11
        if num == 1 or num == 4 or num == 7:
            answer += 'L'
            left = num
        elif num == 3 or num == 6 or num == 9:
            answer += 'R'
            right = num
        else:
            tmpleft = 0
            tmpright = 0
            absleft = 0
            absright = 0
            if left == 1 or left == 4 or left == 7 or left == 10:
                tmpleft = left + 1
                absleft = (abs(tmpleft - num)/3) +1
            else:
                absleft = abs(left-num)/3
            if right == 3 or right == 6 or right == 9 or right == 12:
                tmpright = right - 1
                absright = (abs(tmpright-num)/3) + 1
            else:
                absright = abs(right-num)/3
            if absleft == absright:
                if hand == "right":
                    answer += 'R'
                    right = num
                else:
                    answer += 'L'
                    left = num
            elif absleft > absright:
                right = num
                answer += 'R'
            else:
                left = num
                answer += 'L'
    return answer