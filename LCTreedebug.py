class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # 102 LC
    def levelOrder(self, root):
        # bfs
        if not root:
            return []
        res = []
        queue = [root]

        while queue:
            size = len(queue)
            ires = []
            for i in range(size):
                curr = queue.pop(0)

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

                ires.append(curr.val)
            res.append(ires)

        return res

if __name__ == '__main__':
    x1 = TreeNode(1)
    x2 = TreeNode(2)
    x3 = TreeNode(3)
    x4 = TreeNode(4)
    x5 = TreeNode(5)
    x6 = TreeNode(6)
    x7 = TreeNode(7)
    x8 = TreeNode(8)
    x9 = TreeNode(9)
    x10 = TreeNode(10)
    x11 = TreeNode(11)
    x12 = TreeNode(12)

    x1.left = x2
    x1.right = x3
    x2.left = x4
    x2.right = x5
    x3.left = x6
    x3.right = x7
    x4.left = x8
    x4.right = x9
    x5.left = x10
    x5.right = x11
    x6.left, x6.right = None, None

    print(Solution().levelOrder(x1))