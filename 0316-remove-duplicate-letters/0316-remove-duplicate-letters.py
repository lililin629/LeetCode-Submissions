class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        d = defaultdict(int)
        for i, ch in enumerate(s):
            d[ch] = max(d[ch], i)
        
        ans = []
        for i, ch in enumerate(s):
            if ch in ans:
                continue
            while ans and ord(ans[-1]) > ord(ch) and i < d[ans[-1]]:
                ans.pop()
                
            ans.append(ch)
        
        s = ''.join(ans)
        return s
            
        
            
        
            
            
        