class MinStack:
    def __init__(self):
        self.stack = []
        self.prefix = []
        self.track = float('inf')

    def push(self, val: int) -> None:
        self.track = min(val,self.track)
        self.stack.append(val)
        self.prefix.append(self.track)

    def pop(self) -> None:
        self.stack.pop()
        self.prefix.pop()
        if self.stack:
            self.track = self.prefix[-1]
        else:
            self.track = float('inf')

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.prefix[-1]
