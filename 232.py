class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        self.s1.append(x)
        return
        

    def pop(self) -> int:
        while self.s2:
            cur = self.s2.pop()
            self.s1.append(cur)
        
        while self.s1:
            cur = self.s1.pop()
            self.s2.append(cur)
            
        return self.s2.pop()
        
        

    def peek(self) -> int:
        while self.s2:
            cur = self.s2.pop()
            self.s1.append(cur)
        
        while self.s1:
            cur = self.s1.pop()
            self.s2.append(cur)
        
        return self.s2[-1]
        

    def empty(self) -> bool:
        return len(self.s1) == 0 and len(self.s2) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()