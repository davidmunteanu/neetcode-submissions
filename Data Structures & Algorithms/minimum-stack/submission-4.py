class MinStack:

    def __init__(self):
        self.stack = []
        self.minHistory = [sys.maxsize]

    def push(self, val: int) -> None:
        self.stack.append(val)

        if val <= self.minHistory[-1]:
            self.minHistory.append(val)

        return None

    def pop(self) -> None:
        poppedNum = self.stack.pop()

        if poppedNum == self.minHistory[-1]:
            self.minHistory.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minHistory[-1]
