class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        return ' '.join(s[::-1])
    
    def reverseWords(self, s: str) -> str:
        s = list(s)
        def reverse(start, end):
            while start < end:
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1

       
        reverse(0, len(s) - 1)
        
        start = end = 0
        while start < len(s):
            while start < len(s) and s[start] == ' ':
                start += 1
            end = start
            while end < len(s) and s[end] != ' ':
                end += 1
            
            reverse(start, end - 1)
            start = end
            #print(s)
        print(s)
        i = j = 0
        while i < len(s):
            while i < len(s) and s[i] == ' ':
                i += 1
            while i < len(s) and s[i] != ' ':
                s[j] = s[i]
                i += 1
                j += 1
            if i < len(s) and s[i] == ' ' and j > 0 and s[j-1] != ' ':
                s[j] = ' '
                j += 1
        
        # Remove trailing spaces
        if j > 0 and s[j-1] == ' ':
            j -= 1
        # Convert the list to a string
        return ''.join(s[:j])
    
    