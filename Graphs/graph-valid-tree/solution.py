class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1: return False
        
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        visited = [False] * n

        def dfs(node, parent):
            visited[node] = True
            for neighbor in adj[node]:
                if neighbor == parent:
                    continue
                if visited[neighbor]:
                    return False
                if not dfs(neighbor, node):
                    return False
            return True
        
        dfs(0, -1)
        
        return all(visited)