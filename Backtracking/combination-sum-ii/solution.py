class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
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
            backtrack(idx + 1, total + candidates[idx], curr)
            curr.pop()
            while idx + 1 < len(candidates) and candidates[idx] == candidates[idx + 1]:
                idx += 1
            backtrack(idx + 1, total, curr)

        backtrack(0, 0, [])

        return result