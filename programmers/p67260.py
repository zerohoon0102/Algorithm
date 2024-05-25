from collections import deque

# N < 200,000
# 방문하는 순서 자체를 기록할 필요는 없음. 따라서,
# 조건이 되면 방문할 수 있음을 체크하는 visit, 진짜 방문할 수 있음을 체크할 수 있는 real_visit를 설정
# 진짜 방문할 수 있게 된 cave의 경우에는 queue에 추가
# 방문한 cave를 기록하는 cnt를 통해 cnt의 값에 따라 결과를 리턴
# 조건이 없는 경우에는 queue에 바로 추가할 수 있고, A->B같은 조건인 cave가 있는 경우에는 확인이 필요
# 이를 visit을 통해서 B를 먼저 체크해도 나중에 A를 visit에 체크해도 A와 B를 같이 추가할 수 있음.
# A를 먼저 체크하고 B를 체크하게 될 때도 문제 X
# O(N) + O(len(path)) 와 같은 시간 복잡도를 갖게 됨.
def solution(n, path, order):
    cave_info = [[] for _ in range(n)]
    for a, b in path:
        cave_info[a].append(b)
        cave_info[b].append(a)
    
    order_info = [-1 for _ in range(n)]
    aft_order_info = [-1 for _ in range(n)]
    for a, b in order:
        # 유일한 시작 지점인 0번 동굴이 사전에 다른 동굴 방문이 필요한 경우는 진행 불가능.
        if b == 0:
            return False
        order_info[b] = a
        aft_order_info[a] = b
    
    visit = [False]*n
    visit[0] = True
    real_visit = visit.copy()
    queue = deque([0])
    cnt = n
    while queue:
        cave = queue.popleft()
        for nxt_cave in cave_info[cave]:
            if visit[nxt_cave]:
                continue
            visit[nxt_cave] = True
            if order_info[nxt_cave] == -1 or real_visit[order_info[nxt_cave]]:
                queue.append(nxt_cave)
                real_visit[nxt_cave] = True
            if aft_order_info[nxt_cave] != -1 and visit[aft_order_info[nxt_cave]]:
                queue.append(aft_order_info[nxt_cave])
                real_visit[aft_order_info[nxt_cave]] = True
        cnt -= 1
    if cnt > 0:
        return False
    else:
        return True
