import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    s = input().rstrip()
    mid = len(s)//2
    if len(s)%2 == 0 and s[:mid] == s[mid:][::-1]:
        print(0)
    elif len(s)%2 == 1 and s[:mid] == s[mid+1:][::-1]:
        print(0)
    else:
        chk = False
        left, right = 0, len(s)-1
        arr = [(left, right, 1)]
        while arr:
            left, right, ext = arr.pop()
            if chk:
                break
            while left < right:
                if s[left] == s[right]:
                    if left+1 == right:
                        chk = True
                        break
                    right -= 1
                    left += 1
                elif ext:
                    if len(s)%2 == 0:
                        if right-left == 1:
                            chk = True
                            break
                    if s[left] == s[right-1]:
                        arr.append((left, right-1, 0))
                    if s[left+1] == s[right]:
                        arr.append((left+1, right, 0))
                    break
                else:
                    break
            if left == right:
                chk = True
        if chk:
            print(1)
        else:
            print(2)
