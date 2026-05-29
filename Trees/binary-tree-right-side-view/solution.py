# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        queue = deque()
        queue.append(root)
        result = []

        while queue:
            n = len(queue)
            for i in range(n):
                node = queue.popleft()
                if i == 0:
                    result.append(node.val)
                
                if node.right: queue.append(node.right)
                if node.left: queue.append(node.left)

        return result