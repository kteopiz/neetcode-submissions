class MinStack:

    def __init__(self):
        self.stack = []
        self.minMono = []

    def push(self, val: int) -> None:
        # is this cheating?
        self.stack.append(val)

        temp = []
        if not self.minMono:
            self.minMono.append(val)
        else:
            while self.minMono and val > self.minMono[-1]:
                temp.append(self.minMono.pop())
            self.minMono.append(val)
            while temp:
                self.minMono.append(temp.pop())

    def pop(self) -> None:
        # is this cheating?
        val = self.stack.pop()
        temp = []

        while val != self.minMono[-1]:
            temp.append(self.minMono.pop())
        self.minMono.pop()
        while temp:
            self.minMono.append(temp.pop())


    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minMono[-1]
        
