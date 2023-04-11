class Solution:
    def isValid(self, s: str) -> bool:

        st = []
        c = {')': '(', ']': '[', '}': '{'}

        for i in s:
            if i in ['(', '{', '[']:
                st.append(i)
            else:
                if not st:
                    return False
                check = c[i]
                if check != st[-1]:
                    return False
                st.pop()

        return True if len(st) == 0 else False