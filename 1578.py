from typing import List

class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        res = 0
        st = []
        i = 0
        for color, cost in zip(colors, neededTime):
            ins = True
            # print(color, cost)
            while st and st[-1][0] == color:
                if cost > st[-1][1]:
                    res += st[-1][1]
                    st.pop()
                else:

                    res += cost
                    ins = False
                    # print(st, color, cost, ins)
                    break

            if ins:
                st.append((color, cost))

        print(st)
        return res


if __name__ == '__main__':
    Solution().minCost("aabaa", [1,2,3,4,1])
