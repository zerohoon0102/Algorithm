import sys
from collections import deque

input = sys.stdin.readline    

S = input().rstrip()
cur = ""
tag = False
arr = []
word = []
for s in S:
    if s == "<":
        if cur:
            arr.append(cur)
            word.append(True)
            cur = ""
        cur += s
        tag = True
    elif s == ">":
        cur += s
        tag = False
        arr.append(cur)
        word.append(False)
        cur = ""
    else:
        if tag:
            cur += s
        else:
            if s == " ":
                arr.append(cur)
                word.append(True)
                cur = ""
            else:
                cur += s

if cur:
    arr.append(cur)
    word.append(True)
bef = False
result = ""
for i in range(len(arr)):
    if word[i]:
        if bef:
            result += " "
        result += arr[i][::-1]
    else:
        result += arr[i]
    bef = word[i]
print(result)




