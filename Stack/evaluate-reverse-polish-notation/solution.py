class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {"+", "-", "*", "/"}
        stk = []

        for token in tokens:
            if token in operators:
                a = stk.pop()
                b = stk.pop()

                if token == "+":
                    stk.append(b + a)
                elif token == "-":
                    stk.append(b - a)
                elif token == "*":
                    stk.append(b * a)
                else:
                    stk.append(int(b / a))
            else:
                stk.append(int(token))
        
        return stk[-1]