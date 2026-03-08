class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stk =[]

        for i, h in enumerate(heights):
            start = i
            while stk and stk[-1][1] > h:
               idx, height = stk.pop()
               maxArea = max(maxArea, height * (i - idx))
               start = idx
            stk.append((start, h))
        
        for i, h in stk:
            maxArea = max(maxArea, h * (len(heights) - i))

        return maxArea