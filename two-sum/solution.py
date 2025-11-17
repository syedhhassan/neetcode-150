class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for i, num in enumerate(nums):
            comp = target - num
            if comp in hash:
                return [hash[comp], i]
            hash[num] = i
        return []