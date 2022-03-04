import sys

S = int(sys.stdin.readline().rstrip())

result = 0

start = 1
end = S

while start < end:
    mid = (start+end)//2+1
    total = (mid*(mid+1))//2
    if total > S:
        end = mid-1
    else:
        start = mid

print(start)
