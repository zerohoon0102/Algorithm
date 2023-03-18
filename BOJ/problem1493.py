import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline

info = sorted(map(int, input().rstrip().split()))
need = (info[1]//info[0])*(info[2]//info[1])
target = 0
need_count = [0]*20
while info[0]//(2**target) > 0:
    target += 1

def dfs(length, width, height):
    max_len = 1
    square = 0
    while length//max_len > 1:
        max_len *= 2
        square += 1
    width_max = width//max_len
    height_max = height//max_len
    need_count[square] += width_max*height_max
    if length-max_len > 0:
        nxt_length, nxt_width, nxt_height = sorted([length-max_len, max_len*width_max, max_len*height_max])
        dfs(nxt_length, nxt_width, nxt_height)
    if width-max_len*width_max > 0:
        nxt_length, nxt_width, nxt_height = sorted([max_len, width-max_len*width_max, max_len*height_max])
        dfs(nxt_length, nxt_width, nxt_height)
    if length-max_len > 0 and width-max_len*width_max> 0:
        nxt_length, nxt_width, nxt_height = sorted([length-max_len, width-max_len*width_max, max_len*height_max])
        dfs(nxt_length, nxt_width, nxt_height)
    if height-max_len*height_max > 0:
        nxt_length, nxt_width, nxt_height = sorted([length, width, height-max_len*height_max])
        dfs(nxt_length, nxt_width, nxt_height)

dfs(info[0], info[1], info[2])

n = int(input())
result_count = 0
arr = [0]*20
Fail = False
for _ in range(n):
    i, num = map(int, input().rstrip().split())
    if 2**i > info[0]:
        continue
    arr[i] = num

for i in range(target-1, -1, -1):
    cube = arr[i]
    if cube >= need_count[i]:
        result_count += need_count[i]
        need_count[i] = 0
    else:
        result_count += cube
        need_count[i] -= cube
        if i > 0:
            need_count[i-1] += need_count[i]*8
        else:
            Fail = True
        
            
if Fail:
    print(-1)
else:
    print(result_count)
