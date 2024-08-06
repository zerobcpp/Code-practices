class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        N = len(guess)
        check = [False] * N
        sc = Counter(secret)
        
        a = 0
        b = 0
        for i in range(N):
            if secret[i] == guess[i]:
                a += 1
                sc[guess[i]] -= 1
                check[i] = True
        
        for i in range(N):
            if secret[i] != guess[i] and check[i] != True:
                if guess[i] in sc:
                    if sc[guess[i]] > 0:
                        sc[guess[i]] -= 1
                        b += 1

        return str(a) + 'A' + str(b) + 'B'