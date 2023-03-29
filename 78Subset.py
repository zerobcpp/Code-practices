from collections import defaultdict
class Solution:
    def subsets1(self, nums):
        n = len(nums)
        output = []

        for num in nums:
            temp = []
            for curr in output:
                temp.append(curr + [num])
            for i in temp:
                output.append(i)
        print(output)

        return output

    def subset(self, arr):
        n = len(arr)
        res = defaultdict(int)
        count = 0

        def helper(string, start, end, a):
            nonlocal count
            count += 1
            print(count)
            if len(a) == end:
                res[''.join(a)] += 1

            for i in range(start, len(string)):
                a.append(string[i])
                helper(string, i+1, end, a)
                a.pop()


        arr = arr.split()
        for i in arr:
            i = i.lower()
            for j in range(len(i)):

                helper(i, 0, j, [])

        print(res)
        return res




if __name__ == '__main__':
    print(Solution().subset('Banana String'))
    #print(Solution().subsets([1,2,3]))
