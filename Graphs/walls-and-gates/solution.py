class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m, n = len(grid), len(grid[0])
        q = deque()
        visited = set()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append([i, j])
                    visited.add((i, j))

        def addRoom(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == -1 or (i, j) in visited:
                return
            visited.add((i, j))
            q.append([i, j])

        distance = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = distance
                addRoom(r, c + 1)
                addRoom(r, c - 1)
                addRoom(r + 1, c)
                addRoom(r - 1, c)
            distance += 1
