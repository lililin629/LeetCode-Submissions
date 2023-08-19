class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        d = defaultdict(int)
        for ch in secret:
            d[ch] += 1
        
        cows = 0
        bulls = 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
                d[secret[i]] -= 1
                
        for i in range(len(secret)):
            if guess[i] in d and d[guess[i]] != 0 and guess[i] != secret[i]:
                cows += 1
                d[guess[i]] -= 1
                
        return f"{bulls}A{cows}B"
                
                
        