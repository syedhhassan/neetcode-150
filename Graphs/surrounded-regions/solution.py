class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        def capture(r, c):
            stk = [(r, c)]
            while stk:
                row, col = stk.pop()
                if row < 0 or row >= m or col < 0 or col >= n or board[row][col] != "O":
                    continue
                board[row][col] = "T"
                stk.extend([(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)])
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O" and (i == 0 or i == m - 1 or j == 0 or j == n - 1):
                    capture(i, j)

        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "T":
                    board[i][j] = "O"