"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return

        hashMap = {}

        curr = head
        while curr:
            hashMap[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            new = hashMap[curr]
            new.random = hashMap.get(curr.random)
            new.next = hashMap.get(curr.next)
            curr = curr.next

        return hashMap[head]