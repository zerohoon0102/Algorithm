import sys
from heapq import heappush, heappop
input = sys.stdin.readline

# day 1부터 강연을 할당하는 경우 현재 할당 가능한 강연 중 가장 비용이 큰 강연을 할당하게 되었을 때, 
# [[40,2], [30,1]] 와 같은 케이스에서 day 1에 40을 할당하면서, day1 에 30 day2 에 40 을 할당하는 케이스를 놓치게 됩니다.
# day가 지남에 따라 할당 가능했던 강연을 드랍해야하는 것을 코드에 반영해야하는 비효율이 있습니다.
# 하지만, 마지막 날부터 접근할 경우 현재 진행 가능한 강연으로 추가되면 day가 줄어들어도 드랍해야하는 경우가 없습니다.
# 해당 아고리즘을 통해 O(N)으로 문제를 풀이할 수 있습니다.
N = int(input())
result = 0
if N > 0:
    universities = []
    for _ in range(N):
        universities.append(list(map(int, input().rstrip().split())))
    universities.sort(key=lambda x: -x[1])
    
    can_teach_universities = []
    day = universities[0][1]
    idx = 0
    while day > 0:
        while idx < len(universities) and universities[idx][1] >= day:
            heappush(can_teach_universities, -universities[idx][0])
            idx += 1
        if can_teach_universities:
            result -= heappop(can_teach_universities)
        day -= 1
print(result)
