class MinStack:
    def __init__(self):
        self.stk = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stk.append(val)
        curr_min = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(curr_min)

    def pop(self) -> None:
        self.minStack.pop()
        return self.stk.pop()

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()