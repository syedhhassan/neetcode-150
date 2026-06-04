class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parents = list(range(n + 1))

        def find(node):
            if node != parents[node]:
                parents[node] = find(parents[node])
            return parents[node]
        
        def union(node1, node2):
            parent1, parent2 = find(node1), find(node2)
            if parent1 == parent2:
                return False
            parents[parent1] = parent2
            return True
        
        for a, b in edges:
            if not union(a, b):
                return [a, b]
        
        return []