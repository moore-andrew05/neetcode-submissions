class MinStack:

    def __init__(self):
        self.stk = []
        self.mins = []

    def push(self, val: int) -> None:
        if not self.mins or val < self.mins[-1]:
            curr_min = val
        else:
            curr_min = self.mins[-1]
            

        self.stk.append(val)
        self.mins.append(curr_min)

    def pop(self) -> None:
        self.stk.pop()
        self.mins.pop()
        

    def top(self) -> int:
        return self.stk[-1]
        

    def getMin(self) -> int:
        return self.mins[-1]
        
