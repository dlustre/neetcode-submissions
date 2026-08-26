class MinStack:
    # keep track of two stacks, one normal one and one where nums are only pushed if its smaller than the head

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.minStack:
            self.minStack.append(val)
            return

        if self.minStack[-1] >= val:
            self.minStack.append(val)

    def pop(self) -> None:
        popped = self.stack.pop(-1)

        if self.minStack[-1] == popped:
            self.minStack.pop(-1)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
