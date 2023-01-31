import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline

T = int(input())
mapping = {2: '1', 5: '2', 4: '4', 6:'0', 3: '7', 7:'8'}

for _ in range(T):
    N = int(input())
    s_N = N
    big = ""
    if N%2 == 1:
        big += "7"
        N -= 3
    big += "1"*(N//2)

    small = ""
    sort = sorted(mapping, reverse=True)
    N = s_N
    chk = True
    while chk:
        chk = False
        if N < 8:
            small += mapping[N]
            if N == 6:
                small = '6'
        elif N == 8:
            small = '10' + small
        elif N == 9:
            small = '18' + small
        elif N == 10:
            if small == "":
                small = '22' + small
            else:
                small = '200' + small[1:]
        elif N == 11:
            small = '20' + small
        elif N == 12:
            small = '28' + small
        elif N == 13:
            small = '68' + small
        else:
            small += '8'
            N -= 7
            chk = True
    print(small, big)
