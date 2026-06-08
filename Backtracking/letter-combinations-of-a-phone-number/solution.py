class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)
        result = []
        combinations = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        
        def backtrack(idx, curr):
            if idx == n:
                result.append("".join(curr))
                return

            for letter in combinations[digits[idx]]:
                curr.append(letter)
                backtrack(idx + 1, curr)
                curr.pop()

        backtrack(0, [])

        return result