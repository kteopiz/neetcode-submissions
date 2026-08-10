class MinStack:

    def __init__(self):
        self.stack = []
        self.minMono = []

    def push(self, val: int) -> None:
        # is this cheating?
        self.stack.append(val)

        if not self.minMono:
            self.minMono.append(val)
        else:
            top = self.minMono[-1]
            if val > top:
                self.minMono.append(top)
            else:
                self.minMono.append(val)
    
    def pop(self) -> None:
        # is this cheating?
        self.stack.pop()
        self.minMono.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minMono[-1]
        
