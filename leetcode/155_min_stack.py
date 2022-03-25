class MinStack:

    def __init__(self):
        self.stack = []
        self._min = 1<<31

    def push(self, val: int) -> None:
        self._min = min(self._min, val)
        self.stack.append(val)

    def pop(self) -> None:
        x = self.stack.pop()
        if x == self._min:
            if len(self.stack) > 0:
                self._min = min(self.stack)
            else:
                self._min = 1<<31
        return x
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self._min

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
