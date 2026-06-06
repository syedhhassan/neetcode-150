class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        def backtrack(idx, curr):
            if idx == len(nums):
                result.append(curr[:])
                return
            curr.append(nums[idx])
            backtrack(idx + 1, curr)
            curr.pop()
            while idx + 1 < len(nums) and nums[idx] == nums[idx + 1]:
                idx += 1
            backtrack(idx + 1, curr)

        backtrack(0, [])
        return result
