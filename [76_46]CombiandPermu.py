class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        ans = []
        temp = []
        x = 1
        while True:
            l = len(temp)
            if l == k:
                ans.append(temp.copy())
            if l == k or x > n - k + l + 1:
                if not temp:
                    return ans
                x = temp.pop() + 1
            else:
                temp.append(x)
                x += 1

    def combinev2(self, n, k):
        ans = []
        def bt(start, res):
            if len(res) == k:
                ans.append(res[:])
            else:
                for i in range(start,n+1):
                    res.append(i)
                    bt(i+1, res)
                    res.pop()

        bt(1,[])
        return ans



    def permutation(self, n):
        size = len(n)
        for i in range(n):
            pass




if __name__ == '__main__':
    print(Solution().combinev2(4,2))