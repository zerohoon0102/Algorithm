import sys

N = int(sys.stdin.readline().rstrip())
result = []
stack = []

n = int(sys.stdin.readline().rstrip())
for i in range(1, n+1):
    result.append('+')
    stack.append(i)
result.append('-')
stack.pop()

max_val = n
bef = n
chk = True
for _ in range(N-1):
    n = int(sys.stdin.readline().rstrip())
    if n < bef:
        result.append('-')
        if n != stack.pop():
            chk = False
            break
    else:
        if n < max_val:
            chk = False
            break
        for i in range(max_val+1, n+1):
            result.append('+')
            stack.append(i)
        max_val = n
        result.append('-')
        stack.pop()
        
    bef = n

if chk:
    print('\n'.join(result))
else:
    print('NO')
