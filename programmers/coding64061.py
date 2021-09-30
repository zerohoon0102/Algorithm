def solution(board, moves):
    answer = 0
    backet = []
    len_board = len(board)
    last = 1
    height = [-1] * len_board
    while len_board - last >= 0:
        for a in range(0, len_board):
            if height[a] == -1:
                if board[len_board - last][a] == 0:
                    height[a] = len_board - last + 1
                if len_board - last == 0 and board[len_board - last][a] != 0:
                    height[a] = 0
        last += 1
    for choice in moves:
        if height[choice-1] != len_board:
            if len(backet) == 0:
                backet.append(board[height[choice-1]][choice-1])
            elif len(backet) != 0:
                if backet[len(backet) - 1] == board[height[choice-1]][choice-1]:
                    answer = answer + 2
                    backet.pop()
                else:
                    backet.append(board[height[choice-1]][choice-1])
            height[choice - 1] += 1
                    
    return answer