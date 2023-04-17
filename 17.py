class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        c = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'}

        st = []
        for i in digits:
            st.append(c[i])

        while len(st) > 1:
            d2, d1 = st.pop(), st.pop()
            temp = []
            for i in d1:
                for j in d2:
                    temp.append(i + j)

            st.append(temp)
            # print(st)

        # print(st)
        return st[0] if st else ''
