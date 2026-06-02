class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        EMPTY, FRESH, ROTTEN = 0, 1, 2
        q = deque()
        fresh = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == ROTTEN:
                    q.append((i, j))
                elif grid[i][j] == FRESH:
                    fresh += 1
        
        if fresh == 0: return 0

        minutes = -1
        while q:
            qSize = len(q)
            minutes += 1
            for _ in range(qSize):
                i, j = q.popleft()
                for r, c in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                    if 0 <= r < m and 0 <= c < n and grid[r][c] == FRESH:
                        grid[r][c] = ROTTEN
                        fresh -= 1
                        q.append((r, c))

        return minutes if fresh == 0 else -1