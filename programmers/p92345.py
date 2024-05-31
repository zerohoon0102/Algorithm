i_dir = [1,-1,0,0]
j_dir = [0,0,1,-1]


# A에게 시작 우선권이 있다는 점에 초점을 두어야 한다.
# A의 차례에서 갈 수 있는 경우의 수 중 하나라도 A가 이기는 경우의 수가 있으면 A가 실수만 없으면 이길 수 있다. B에 맞춰서 갈 수 있기 때문에
# 반면에 B의 차례에는 B가 갈 수 있는 경우의 수 모두가 A가 이겨야 A가 실수 없으면 이길 수 있는 케이스다.
# 그런데 만약 A가 실수만 없어도 무조건 이기는 경우가 없다면?
# 후발 주자인 B가 A에 맞추어서 움직일 수 있으므로 실수만 없다면 무조건 B가 이기게 되어 있음을 파악해야한다.
# 그런데, 그렇다고 해도 이동 횟수는 어떻게 파악하지?
# 각 차례에서 A가 이기는 경우에 대한 A의 최소값과 B가 이기는 경우에 대한 최소값을 트래킹하고
# 이를 실수 없으면 이기는 플레이어의 값으로 리턴한다.
# 꽤나 푸는데 오래 걸렸다. 무조건 이길 수 있는 플레이어를 찾는 코드는 빨리 구현했지만, 그 와중에 최소 이동횟수를 어떻게 찾을지를
# 떠올리는데 오래 걸렸다.
def dfs(cnt:int, user: int, user_place:  list, board: list):
    cur_i, cur_j = user_place[user]
    if board[cur_i][cur_j] == 0:
        return abs(user-1), cnt
    board[cur_i][cur_j] = 0
    chk = 0 if user == 1 else 1
    
    chk_can_move = False
    min_cnt = [1000,1000]
    for direc in range(4):
        nxt_i = cur_i + i_dir[direc]
        nxt_j = cur_j + j_dir[direc]
        if 0 <= nxt_i < len(board) and 0 <= nxt_j < len(board[0]) and board[nxt_i][nxt_j]:
            user_place[user] = [nxt_i, nxt_j]
            winner, cur_cnt = dfs(cnt+1, abs(user-1), user_place, board)
            # if cnt == 0:
            #     print(nxt_i, nxt_j, ":", winner, cur_cnt)
            if user == 1:
                chk = chk or winner
                if winner == 1:
                    min_cnt[winner] = min(min_cnt[winner], cur_cnt)
                else:
                    if min_cnt[winner] == 1000:
                        min_cnt[winner] = cur_cnt
                    else:
                        min_cnt[winner] = max(min_cnt[winner], cur_cnt)
            else:
                chk = chk and winner
                if winner == 0:
                    min_cnt[winner] = min(min_cnt[winner], cur_cnt)
                else:
                    if min_cnt[winner] == 1000:
                        min_cnt[winner] = cur_cnt
                    else:
                        min_cnt[winner] = max(min_cnt[winner], cur_cnt)
            chk_can_move = True
    
    board[cur_i][cur_j] = 1
    if chk_can_move:
        user_place[user] = [cur_i, cur_j]
    else:
        return abs(user-1), cnt
    
    return chk, min_cnt[chk]

def solution(board, aloc, bloc):
    user_place = [bloc, aloc]
    user_dist = [30, 30]
    
    winner, answer = dfs(cnt=0, user=1, user_place=user_place, board=board)
    print(winner)
    return answer
