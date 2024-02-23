class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        collection = []
        for i in s:
            if i in "{([":
                collection.append(i)

            if i in "})]":
                a = collection.pop()
                return (a == "(" and i == ")") or (a == "{" and i == "}") or (a == "{" and i == "}")
