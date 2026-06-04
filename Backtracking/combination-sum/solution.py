class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(idx, total, curr):
            if total == target:
                result.append(curr[:])
                return
            if total > target:
                return
            if idx == len(candidates):
                return

            curr.append(candidates[idx])
            backtrack(idx, total + candidates[idx], curr)
            curr.pop()
            backtrack(idx + 1, total, curr)
        
        backtrack(0, 0, [])
        
        return result