class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        string = []
        for i in range(1,n+1,1):
            if i % 15 == 0:
                string.append("FizzBuzz")
            elif i % 5 == 0:
                string.append("Buzz")
            elif i % 3 == 0:
                string.append("Fizz")
            else:
                string.append(str(i))
        
        return string