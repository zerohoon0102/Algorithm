def same_side(m,n,col, row, board, del_list):
    r = False
    c = False
    rc = False
    rc2 = False
    if row < n - 2 :
        if board[col][row] == board[col][row+2] and board[col][row] == board[col+1][row+2]:
            del_list.append(f"{col},{row+2}")
            del_list.append(f"{col+1},{row+2}")
            r = True
    if col < m - 2 :
        if board[col][row] == board[col+2][row] and board[col][row] == board[col+2][row+1]:
            del_list.append(f"{col+2},{row}")
            del_list.append(f"{col+2},{row+1}")
            c = True
    
    if col < m - 2 and row < n - 2:
        if board[col][row] == board[col+2][row+1] and board[col][row]==board[col+2][row+2] and board[col][row] == board[col+1][row+2] and board[col][row] != board[col+2][row]:
            del_list.append(f"{col+2},{row+1}")
            del_list.append(f"{col+1},{row+2}")
            del_list.append(f"{col+2},{row+2}")
            rc = True

    if col < m - 2 and row > 0:
        if board[col][row] == board[col+1][row-1] and board[col][row]==board[col+2][row-1] and board[col][row] == board[col+2][row] and board[col][row] != board[col+2][row+1]:
            del_list.append(f"{col+1},{row-1}")
            del_list.append(f"{col+2},{row-1}")
            del_list.append(f"{col+2},{row}")
            rc2 = True
    if r :
        same_side(m,n,col,row+1,board, del_list)
    if c :
        same_side(m,n,col+1,row,board,del_list)
    if rc:
        same_side(m,n,col+1,row+1,board,del_list)
    if rc2:
        same_side(m,n,col+1,row-1,board,del_list)
    if r:
        board[col] = board[col][0:row+2] + "-" + board[col][row+3:n]
        board[col+1] = board[col+1][0:row+2] + "-" + board[col+1][row+3:n]
    if c:
        board[col+2] = board[col+2][0:row] + "--" + board[col+2][row+2:n]
    if rc:
        board[col+2] = board[col+2][0:row+1] + "--" + board[col+2][row+3:n]
        board[col+1] = board[col+1][0:row+2] + "-" + board[col+1][row+3:n]
    if rc2:
        board[col+2] = board[col+2][0:row-1] + "--" + board[col+2][row+1:n]
        board[col+1] = board[col+1][0:row-1] + "-" + board[col+1][row:n]

def sort_board(m,n,board):
    for row in range(0, n):
        lowest_pos = m
        col = m - 1
        while col >= 0:
            if board[col][row] == "-":
                if lowest_pos == m or lowest_pos < col:
                    lowest_pos = col
            else:
                if lowest_pos < m and lowest_pos >= 0:
                    board[lowest_pos] = board[lowest_pos][0:row] + board[col][row] + board[lowest_pos][row+1:n]
                    board[col] = board[col][0:row] + "-" + board[col][row+1:n]
                    temp_col = m-1
                    while temp_col >= 0:
                        if board[temp_col][row] == "-":
                            break
                        temp_col = temp_col - 1
                    lowest_pos = temp_col
            col = col - 1

def solution(m, n, board):
    answer = 0
    del_list = ["a"]
    while len(del_list) != 0:
        del_list = []
        for col in range(0, m - 1):
            for row in range(0, n-1):
                if board[col][row] == "-":
                    pass
                elif board[col][row] == board[col+1][row+1] and board[col][row] == board[col+1][row] and board[col][row] == board[col][row + 1]:
                    del_list.append(f"{col},{row}")
                    del_list.append(f"{col},{row+1}")
                    del_list.append(f"{col+1},{row}")
                    del_list.append(f"{col+1},{row+1}")
                    same_side(m,n, col, row, board, del_list)
                    board[col] = board[col][0:row] + "--" + board[col][row+2:n]
                    board[col+1] = board[col+1][0:row] + "--" + board[col+1][row+2:n]
        del_list = set(del_list)
        del_list = list(del_list)
        sort_board(m,n,board)
        print(board)
        answer = answer + len(del_list)
    
    return answer