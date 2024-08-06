class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        N = len(deck)
        st = deque(list(range(N)))
        print(st)
        res = [0] * N 
        for i in range(N-1):
            cur = st.popleft()
            st.append(st.popleft())
            res[cur] = deck[i]
        
        res[st[0]] = deck[-1]
        return res
            
        

        
"""
[17,13,11,2,3,5,7]
[2,13,3,11,5,17,7]

[3,1,4,2,5,0,6]


[2, 3, 5, 7, 11, 13, 17]
[2,13,3,11,5,17,7]
[0,2,4,6,3,1,5]

"""