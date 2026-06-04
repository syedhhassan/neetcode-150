class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            adj[b].append(a)

        UNVISITED, VISITING, VISITED = 0, 1, 2
        states = [UNVISITED] * numCourses

        def dfs(node):
            if states[node] == VISITED: return True
            if states[node] == VISITING: return False

            states[node] = VISITING
            for neighbor in adj[node]:
                if not dfs(neighbor):
                    return False
            states[node] = VISITED
            return True
        
        return all(dfs(i) for i in range(numCourses))
