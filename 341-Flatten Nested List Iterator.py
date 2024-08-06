# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.st = [[nestedList, 0]]
        #self.n = len(nestedList)
        #self.cur = 0
        
        
    def next(self) -> int:
        self.hasNext()
        lst, idx = self.st[-1]
        self.st[-1][1] += 1
        return lst[idx].getInteger()
        
    
    def hasNext(self) -> bool:
        
        
        while self.st:
            lst, cur = self.st[-1]
            
            if cur == len(lst):
                self.st.pop()
            else:
                v = lst[cur]
                if v.isInteger():
                    return True
                self.st[-1][1] += 1
                self.st.append([v.getList(), 0])
        return False
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())