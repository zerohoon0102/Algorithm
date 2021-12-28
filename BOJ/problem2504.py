import sys
from collections import deque, Counter

input_str = sys.stdin.readline().rstrip()

counter = Counter(input_str)
if (counter["("] != counter[")"]) or (counter["["] != counter["]"]):
    print(0)
else:
    stack = []
    count = {"(": 0, "[": 0}

    result = 0
    chk = True
    for i, c in enumerate(input_str):
        if c == "(" or c == "[":
            stack.append(c)
            count[c] += 1
        else:
            if len(stack) > 0:
                recent = stack.pop()
                if recent == "(":
                    if c == ")":
                        count[recent] -= 1
                        if input_str[i-1] == "(":
                            result += 2*(2**count["("])*(3**count["["])
                    else:
                        chk = False
                        break
                else:
                    if c == "]":
                        count[recent] -= 1
                        if input_str[i-1] == "[":
                            result += 3*(3**count["["])*(2**count["("])
                    else:
                        chk = False
                        break
            else:
                chk = False
                break
    if chk:
        print(result)
    else:
        print(0)
                
