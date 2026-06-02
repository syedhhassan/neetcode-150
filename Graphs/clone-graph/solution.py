"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        hashMap = {}
        stk = [node]
        hashMap[node] = Node(node.val)

        while stk:
            curr = stk.pop()
            for neighbor in curr.neighbors:
                if neighbor not in hashMap:
                    hashMap[neighbor] = Node(neighbor.val)
                    stk.append(neighbor)
        
        for old, new in hashMap.items():
            for neighbor in old.neighbors:
                new.neighbors.append(hashMap[neighbor])
        
        return hashMap[node]