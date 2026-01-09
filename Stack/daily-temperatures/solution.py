class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n
        stk = []

        for i in range(n):
            while stk and temperatures[stk[-1]] < temperatures[i]:
                idx = stk.pop()
                result[idx] = i - idx
            stk.append(i)

        return result
