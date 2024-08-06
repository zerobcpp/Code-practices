class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        N = len(books)
        def helper(i, width, height):
            if i >= N:
                return 0
            w, h = books[i]
            
            advance = h + helper(i+1, w, h)
            stay = float('inf')
            if width + w <= shelfWidth:
                height_inc = max(0, h - height)
                stay = min(stay,  height_inc + helper(i+1, width + w, height_inc + height))
            
            return min(stay, advance)
        
        return helper(0, 0, 0)
    
    
    def minHeightShelves(self, book, k):
        N = len(book)
        cache = {}
        def helper(i):
            if i >= N:
                return 0
            if i in cache:
                return cache[i]
            
            idx = i
            width, height, need = 0, 0, float('inf')
            while idx < N and width + book[idx][0] <= k:
                height = max(height, book[idx][1])
                width += book[idx][0]
                idx += 1
                need = min(need, height + helper(idx))
            
            cache[i] = need
            return need
        
        
        return helper(0)