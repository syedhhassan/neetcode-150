class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []

        def backtrack(curr, visited):
            if len(curr) == n:
                result.append(curr[:])
                return
            
            for i in range(n):
                if not visited[i]:
                    curr.append(nums[i])
                    visited[i] = True
                    backtrack(curr, visited)
                    curr.pop()
                    visited[i] = False

        backtrack([], [False] * n)

        return result