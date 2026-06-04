class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            adj[b].append(a)

        UNVISITED, VISITING, VISITED = 0, 1, 2
        states = [UNVISITED] * numCourses

        order = []

        def dfs(node):
            if states[node] == VISITED: return True
            if states[node] == VISITING: return False

            states[node] = VISITING
            for neighbor in adj[node]:
                if not dfs(neighbor):
                    return False
            states[node] = VISITED
            order.append(node)
            return True
        
        return order[::-1] if all(dfs(i) for i in range(numCourses)) else []