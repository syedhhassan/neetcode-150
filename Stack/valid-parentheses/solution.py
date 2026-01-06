class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        hash = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }

        for c in s:
            if c in hash:
                if stk and stk[-1] == hash[c]:
                    stk.pop()
                else:
                    return False
            else:
                stk.append(c)

        return True if not stk else False