from collections import deque


def findAllChar(board, letter):
    coordinates = []
    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] == letter:
                coordinates.append((r, c))
    return coordinates

def getAdjCells(cell, board):
    """
    Return the coordinates of all adjacent cells
    """
    r, c = cell
    
    directions = [(r, c+1), (r, c-1), (r+1, c), (r-1, c)]
    
    return [(i, j) for i, j in directions
           if 0<=i<len(board) and 0<=j<len(board[0])]
                
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        allStartingPoints = findAllChar(board, word[0])
        
        if len(allStartingPoints) == 0:
            return False
        elif len(word) == 1:
            # Check for this edge case
            return True
        
        allLetters = [board[r][c] for r in range(len(board)) for c in range(len(board[0]))]
        if len(set(allLetters)) < len(set(list(word))):
            # Check for edge case where the letters do not exists in the board
            return False
        
        for startingPoint in allStartingPoints:
            parents = set()
            parents.add(startingPoint)
            queue = deque([(startingPoint, 0, parents)])
            
            while queue:
                cell, level, parents = queue.pop()
                
                for adjCell in getAdjCells(cell, board):
                    r, c = adjCell
                    if board[r][c] == word[level + 1] and adjCell not in parents:
                        adjParents = parents.copy()
                        adjParents.add(adjCell)
                        
                        if level + 1 == len(word) - 1:
                            return True
                        queue.appendleft((adjCell, level + 1, adjParents))
                    
        return False 