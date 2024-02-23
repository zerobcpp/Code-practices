class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        inside = 0
        total = 0
        st = [(row, column, k)]
        directions = [
            (1, 2),
            (2, 1),
            (2, -1),
            (1, -2),
            (-2, -1),
            (-1, -2),
            (-2, 1),
            (-1, 2)
        ]
        
        @cache
        def helper(left, i, j):
            if left == 0:
                if i == row and j == column:
                    return 1
                else:
                    return 0
            
            count = 0
            for cx, cy in directions:
                dx = i + cx
                dy = j + cy
                
                if 0 <= dx < n and 0 <= dy < n:
                    count += helper(left - 1, dx, dy)
            
            #print(count)
            return count / 8
        
        prob = 0
        for i in range(n):
            for j in range(n):
                prob += helper(k, i, j)
        
        return prob
        
                
        
        
#         while st: 
#             x, y, left = st.pop()
#             if x == row and y == column: 
#                 inside += 1
#                 total += 1
            
#             elif ((x >= n or x < 0) or (y >= n or y < 0)):
#                 total += 1
            
#             for cx, cy in directions:
#                 dx = x + cx
#                 dy = y + cy
#                 if left > 0:
#                     st.append((dx, dy, left - 1))
        
#         print(inside, total)
#         print(inside/total)
                
            
        
        