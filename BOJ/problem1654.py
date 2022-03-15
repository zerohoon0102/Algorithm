import sys

K, N = map(int, sys.stdin.readline().rstrip().split())

wire = []
for _ in range(K):
    wire.append(int(sys.stdin.readline().rstrip()))

start = 0
end = max(wire)

def chk(arr, n):
    count = 0
    for s in arr:
        count += s//n
    if count >= N:
        return True
    else:
        return False

while end > start:
    mid = (start+end)//2 + 1
    print(f"start: {start}, end: {end}, mid: {mid}")
    if chk(wire, mid):
        start = mid
    else:
        end = mid-1
    

print(end)
