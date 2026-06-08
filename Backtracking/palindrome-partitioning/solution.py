class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        result = []

        def isPalindrome(s):
            l, r = 0, len(s) - 1
            while l <= r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        def backtrack(idx, curr):
            if idx == n:
                result.append(curr[:])
                return
            
            for end in range(idx, n):
                if isPalindrome(s[idx : end + 1]):
                    curr.append(s[idx : end + 1])
                    backtrack(end + 1, curr)
                    curr.pop()

        
        backtrack(0, [])

        return result