class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head) -> bool:
        try:
            slow = head.next
            fast = head.next.next
            while slow != fast:
                slow = slow.next
                fast = fast.next.next
            return True
        except:
            return False


if __name__ == '__main__':
    x = [3, 2, 0, -4]
    # 1
    # [1, 2]
    # 0
    # [1]

    c = ListNode(x[0])
    dummy = c
    for i in range(1, len(x)):
        c.next = ListNode(x[i])
        c = c.next
    c.next = dummy.next

    print(Solution().hasCycle(dummy))
