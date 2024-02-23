class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        N = len(guess)
        
        sc = Counter(secret)
        gc = Counter(guess)
        
        a = 0
        b = 0
        for i in range(N):
            if secret[i] == guess[i]:
                a += 1
                sc[guess[i]] -= 1
            else:
                if guess[i] in sc:
                    if sc[guess[i]] > 0:
                        sc[guess[i]] -= 1
                        b += 1
        
        
        return str(a) + 'A' + str(b) + 'B'