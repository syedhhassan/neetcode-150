class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(p, (target - p) / s) for p, s in zip(position, speed)]
        pairs.sort(reverse=True)
        stk = []

        for p, time in pairs:
            stk.append(time)
            if len(stk) >= 2 and stk[-1] <= stk[-2]:
                stk.pop()

        return len(stk)