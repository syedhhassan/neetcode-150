class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0

        l, r = 0, len(height) - 1
        lMax, rMax = height[l], height[r]
        trapped = 0

        while l < r:
            if lMax < rMax:
                l += 1
                lMax = max(lMax, height[l])
                trapped += lMax - height[l]
            else:
                r -= 1
                rMax = max(rMax, height[r])
                trapped += rMax - height[r]
        
        return trapped