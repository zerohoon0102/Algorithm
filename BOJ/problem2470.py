import sys
input = sys.stdin.readline

N = int(input())
minus = []
plus = []
zero = False
for n in map(int, input().rstrip().split()):
    if n < 0:
        minus.append(n)
    elif n > 0:
        plus.append(n)
    else:
        zero = True

minus.sort(reverse=True)
plus.sort()
if not minus:
    if zero:
        result = [0, plus[0]]
    else:
        result = [plus[0], plus[1]]
elif not plus:
    if zero:
        result = [minus[0], 0]
    else:
        result = [minus[1], minus[0]]
else:
    value = None
    if zero:
        result = [0, plus[0]]
        value = plus[0]
        if abs(minus[0]) < value:
            value = abs(minus[0])
            result = [minus[0], 0]
    else:
        if len(plus) > 1:
            result = [plus[0], plus[1]]
            value = sum(result)
        if len(minus) > 1:
            if value == None or value > abs(minus[0]+minus[1]):
                result = [minus[1], minus[0]]
                value = abs(sum(result))
    m = minus.pop()
    p = plus.pop()
    
    if value == None or abs(m+p) < value:
        result = [m, p]
        value = abs(m+p)

    while minus or plus:
        if (m+p < 0 and minus) or not plus:
            m = minus.pop()
        else:
            p = plus.pop()
        if value > abs(m+p):
            result = [m,p]
            value = abs(m+p)
print(result[0], result[1])
