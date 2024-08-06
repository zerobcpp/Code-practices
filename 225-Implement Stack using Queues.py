class MyStack:

    def __init__(self):
        self.q = Queue()

    def push(self, x: int) -> None:
        self.q.queue(x)
    
    def pop(self) -> int:
        return self.q.dequeue()

    def top(self) -> int:
        return self.q.peek()

    def empty(self) -> bool:
        return self.q.empty()

class Node:
    
    def __init__(self, v):
        self.v = v
        self.next = None
        

class Queue:
    
    def __init__(self):
        self.tail = Node(-1)
        self.head = Node(-1)
        self.head.next = self.tail
    
    def queue(self, v):
        n = Node(v)
        n.next = self.head.next
        self.head.next = n
    
    def dequeue(self):
        x = self.head.next.v
        self.head.next = self.head.next.next
        return x
    
    def peek(self):
        return self.head.next.v
    
    def empty(self):
        self.dbg()
        return self.head.next.v == -1
    
    def dbg(self):
        x = self.head
        while x:
            print(x.v, end = '\t')
            x = x.next
    
    
        

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()