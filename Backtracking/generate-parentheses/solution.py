class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        OPEN, CLOSE = "(", ")"
        result = []

        def backtrack(open, close, curr):
            if len(curr) == 2 * n:
                result.append("".join(curr))
                return
            
            if open < n:
                curr.append(OPEN)
                backtrack(open + 1, close, curr)
                curr.pop()
            
            if close < open:
                curr.append(CLOSE)
                backtrack(open, close + 1, curr)
                curr.pop()
            
        backtrack(0, 0, [])

        return result