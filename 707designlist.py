class MyLinkedList:

    def __init__(self):
        self.head = Node(-9)
        self.length = 0

    def get(self, index: int) -> int:
        i = 0
        cur = self.head.next
        while i < index:
            cur = cur.next
            i += 1
        return cur.val

    def addAtHead(self, val: int) -> None:
        n = Node(val)
        n.next = self.head.next
        self.head.next = n
        self.length += 1

    def addAtTail(self, val: int) -> None:
        cur = self.head.next
        i = 0
        while i < self.length - 1:
            cur = cur.next
            i += 1
        n = Node(val)
        cur.next = n
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        n = self.head.next
        # print(n.next.val)
        i = 0
        while i < index - 1:
            n = n.next
            i += 1
        # print(n.val)
        temp = n.next
        new_node = Node(val)
        n.next = new_node
        new_node.next = temp
        self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        if index == 0 and self.length < 2:
            self.head.next = None
            self.length -= 1
            return None
        elif index == 0:
            self.head.next = self.head.next.next
            self.length -= 1
            return None
        i = 0
        cur = self.head.next
        while i < index - 1:
            cur = cur.next
            i += 1
        # print(cur.val, cur.next.val, cur.next.next.val)
        cur.next = cur.next.next
        self.length -= 1

    def debug(self) -> None:
        n = self.head
        for i in range(self.length+1):
            print(n.val, end='->')
            n = n.next
        print()


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


obj = MyLinkedList()

obj.addAtHead(1)
obj.addAtTail(3)
obj.addAtIndex(1, 2)
obj.debug()
print(obj.get(1))
obj.deleteAtIndex(0)
obj.debug()
print(obj.get(0))


#
# ["MyLinkedList","addAtHead","addAtTail","addAtIndex","get","deleteAtIndex","get"]
# [[],[1],[3],[1,2],[1],[0],[0]]