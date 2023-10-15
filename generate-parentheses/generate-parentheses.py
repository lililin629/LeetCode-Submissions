class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
      
        if n == 0:
            return ['']
        if n == 1:
            return ['()']
        ans = []
        
        for p in self.generateParenthesis(n-1):
            for i in range(len(p)):
                ans.append(p[0:i]+'()'+p[i:])
        return list(set(ans))
            
            
        
        
        
        
        