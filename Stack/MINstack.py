class MinStack:

    def __init__(self):
       self.stack=[]
        

    def push(self, value: int) -> None:
        if len(self.stack)==0:
            self.stack.append((value,value)) # Storing the element and its min value i.e (value,min) in tuples in that list so that it is 0(1)
        else:
            minimum=min(value,self.stack[-1][1])
            self.stack.append((value,minimum))

    def pop(self) -> None:
        return self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        return self.stack[-1][1]

        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()