class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.word_dict = {}
        self.board = board
        self.N = len(board)
        self.M = len(board[0])
        self.ver_direc = [0,0,-1,1]
        self.hor_direc = [-1,1,0,0]

        cur_word_dict = self.word_dict
        for word in words:
            for s in word:
                if s not in cur_word_dict:
                    cur_word_dict[s] = {}
                cur_word_dict = cur_word_dict[s]
            cur_word_dict['value'] = word
            cur_word_dict = self.word_dict
        
        self.result = []
        for i in range(self.N):
            for j in range(self.M):
                cell = self.board[i][j]
                if cell in self.word_dict:
                    self.dfs(i,j,{}, self.word_dict[cell])

        return self.result
    
    def dfs(self, i, j, chk_board, cur_word_dict):
        chk_board[(i,j)] = False
        if 'value' in cur_word_dict:
            self.result.append(cur_word_dict['value'])
            del cur_word_dict['value']

        for idx in range(4):
            nxt_i = i+self.ver_direc[idx]
            nxt_j = j+self.hor_direc[idx]
            if 0 <= nxt_i < self.N and 0 <= nxt_j < self.M and ((nxt_i, nxt_j) not in chk_board):
                cell = self.board[nxt_i][nxt_j]
                if cell in cur_word_dict:
                    self.dfs(nxt_i, nxt_j, chk_board.copy(), cur_word_dict[cell])
                    if len(cur_word_dict[cell]) == 0:
                        del cur_word_dict[cell]
        return 0
