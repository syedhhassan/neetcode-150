class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return max(nums[0], nums[1])

        def money(i, j):
            one, two = nums[i], max(nums[i], nums[i + 1])
            for idx in range(i + 2, j + 1):
                one, two = two, max(nums[idx] + one, two)
            return two
        
        return max(money(0, n - 2), money(1, n - 1))