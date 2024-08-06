class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        collection = []
        truecollection = []
        for i in s:
            if i in "{([":
                collection.append(i)
                if(len(s)==1):
                    return False
                elif len(s)%2 != 0:
                    return False

            if i in "})]":
                try:
                    a = collection.pop()
                    if (a == "(" and i == ")") or (a == "[" and i == "]") or (a == "{" and i == "}"):
                        truecollection.append(True)
                    else:
                        truecollection.append(False)
                except IndexError:
                    truecollection.append(False)
        
        if not truecollection or collection:
            return False
        return all(truecollection)