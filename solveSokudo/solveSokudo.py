class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if(board == None or len(board) != 9 or len(board[0]) !=9):  
            return;
        tmp = []
        for e in board:
            tmp.append(list(e))
        self.helper(tmp, 0, 0)
        print tmp
    def helper(self, board, i, j):
        if j == 9:
            return self.helper(board, i+1, 0)
        if i == 9:
            return True
        if board[i][j] == '.':
            for k in range(1,10):
                board[i][j] = str(k)
                if self.isValid(board, i, j):
                    if self.helper(board, i, j+1):
                        return True
                board[i][j] = '.'
        else:
            return self.helper(board,i,j+1)
        return False
                

        
    def isValid(self, board, x, y):
        for i in range(9):  
            if(i != x and board[i][y] == board[x][y]):
                return False
        for j in range(9):
            if(j != y and board[x][j] == board[x][y]):
                return False
        for i in range(3 * (x / 3), 3 * (x / 3 + 1)):  
            for j in range(3 * (y / 3), 3 * (y / 3 + 1)): 
                if ((i != x or j != y) and board[i][j] == board[x][y]) : 
                    return False 
        return True 
sol = Solution()
sol.solveSudoku(["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."])
