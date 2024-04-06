answer = 1000
minimum = 0
def deep_copy(board):
    boards = [[board[i][j] for j in range(4)] for i in range(4)]
    return boards

def c_dfs(boards, row, col, r, c,rows, cols, e_i, e_j):
    global minimum
    if r == e_i and c == e_j:
        if rows[1]+cols[1] < minimum:
            minimum = rows[1]+cols[1]
    else:
        c_c = c
        if c_c != e_j:
            c_c += col
            c_rows = rows.copy()
            c_cols = cols.copy()
            if c_rows[0] > 0:
                c_rows[1] += c_rows[0]
                c_rows[0] = 0
            if boards[r][c_c] == 0:
                c_cols[0] += 1
            if boards[r][c_c] != 0 or c_c == 0 or c_c == 3:
                c_cols[0] = 0
                c_cols[1] += 1
            c_dfs(boards, row, col, r, c_c, c_rows, c_cols, e_i, e_j)
        if r != e_i:
            r += row
            r_rows = rows.copy()
            r_cols = cols.copy()
            if r_cols[0] > 0:
                r_cols[1] += r_cols[0]
                r_cols[0] = 0
            if boards[r][c] == 0:
                r_rows[0] += 1
            if boards[r][c] != 0 or r == 0 or r == 3:
                r_rows[0] = 0
                r_rows[1] += 1
            c_dfs(boards, row, col, r, c, r_rows, r_cols, e_i, e_j)

def count(boards, s_i, s_j, e_i, e_j):
    global minimum
    minimum = 100
    row = 1 if s_i < e_i else -1
    col = 1 if s_j < e_j else -1
    c_dfs(boards, row, col, s_i, s_j,[0,0], [0,0], e_i, e_j)
    return minimum

def dfs(boards, cards, row, col, tmp):
    global answer
    if boards[row][col] == 0:
        rows = []
        cols = []
        for i in range(4):
            if row != i:
                rows.append(i)
            if col != i:
                cols.append(i)
        for i in rows:
            if boards[i][col] != 0:
                dfs(deep_copy(boards), cards.copy(), i, col, tmp+count(boards, row, col, i, col))
        for i in cols:
            if boards[row][i] != 0:
                dfs(deep_copy(boards), cards.copy(), row, i, tmp+count(boards, row, col, row, i))
        for i in rows:
            for j in cols:
                if boards[i][j] != 0:
                    dfs(deep_copy(boards), cards.copy(), i, j, tmp+count(boards, row, col, i, j))
    else:
        num = boards[row][col]
        boards[row][col] = 0
        row_a, col_a = cards[num][[row,col] == cards[num][0]]
        tmp += count(boards, row, col, row_a, col_a)
        row, col = row_a, col_a
        boards[row][col] = 0
        del cards[num]
        if len(cards) > 0:
            dfs(deep_copy(boards), cards.copy(), row, col, tmp)
        else:
            if tmp < answer:
                answer = tmp


def solution(board, r, c):
    global answer
    n = 4
    card_list = {}
    for i in range(n):
        for j in range(n):
            num = board[i][j]
            if num != 0:
                if num in card_list:
                    card_list[num].append([i,j])
                    a_i, a_j = card_list[num][0]
                    card_list[num].append(1 if i == a_i or j == a_j else 2)
                else:
                    card_list[num] = [[i,j]]
    cnt = 2*len(card_list)
    dfs(board, card_list, r, c, 0)
    answer += cnt
    return answer
