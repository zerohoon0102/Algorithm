import sys

N = int(sys.stdin.readline().rstrip())
n_arr = set(sys.stdin.readline().rstrip().split())

M = int(sys.stdin.readline().rstrip())
m_arr = sys.stdin.readline().rstrip().split()

result = ''


j = 0
for s in m_arr:
    if s in n_arr:
        result += '1 '
    else:
        result += '0 '

print( result.rstrip() )
