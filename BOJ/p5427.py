import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

i_dir = [0, 0, 1, -1]
j_dir = [1, -1, 0, 0]

IMPOSSIBLE = 10**9
# bfs
def find_door(i: int, j: int, chk_board: list, fire_map: list):
    result = IMPOSSIBLE
    H, W = len(chk_board), len(chk_board[0])

    cur_point = [(i,j)]
    nxt_point = []
    time = 0
    while cur_point:
        for _ in range(len(cur_point)):
            i, j = cur_point.pop()
            if i == 0 or i == H-1 or j == 0 or j == W-1:
                result = min(result, time+1)
            else:
                for n in range(4):
                    nxt_i, nxt_j = i+i_dir[n], j+j_dir[n]
                    if chk_board[nxt_i][nxt_j] and fire_map[nxt_i][nxt_j] > time+1:
                        chk_board[nxt_i][nxt_j] = False
                        nxt_point.append((nxt_i, nxt_j))
        cur_point = nxt_point
        nxt_point = []
        time += 1
                
    return result

# main
def solution():
    T = int(input())
    for _ in range(T):
        W, H = map(int, input().rstrip().split())
        building = []
        for __ in range(H):
            building.append(input().rstrip())
        
        fire_map = [[IMPOSSIBLE]*W for __ in range(H)]
        chk_board = [[True]*W for __ in range(H)]
        cur_fire = []
        for i in range(H):
            for j in range(W):
                v = building[i][j]
                if v == '@':
                    start_i, start_j = i, j
                elif v == '*':
                    cur_fire.append((i,j))
                    fire_map[i][j] = 0
                elif v == '#':
                    chk_board[i][j] = False
        
        time = 1
        while cur_fire:
            nxt_fire = []
            for i, j in cur_fire:
                for n in range(4):
                    nxt_i, nxt_j = i+i_dir[n], j+j_dir[n]
                    if 0 <= nxt_i < H and 0 <= nxt_j < W and chk_board[nxt_i][nxt_j] and fire_map[nxt_i][nxt_j] == IMPOSSIBLE:
                        fire_map[nxt_i][nxt_j] = time
                        nxt_fire.append((nxt_i, nxt_j))
            time += 1
            cur_fire = nxt_fire

        chk_board[start_i][start_j] = False
        result = find_door(start_i, start_j, chk_board, fire_map)
        if result == IMPOSSIBLE:
            print("IMPOSSIBLE")
        else:
            print(result)
        
solution()
