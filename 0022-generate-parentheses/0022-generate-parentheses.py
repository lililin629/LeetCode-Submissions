class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        ps = []
        self.dfs('', n, ps, 0, 0)
        return ps
    
    def dfs(self, p, n, ps, ocount, ccount):
        if len(p) == 2*n:
            ps.append(p)
            return
        if ocount < n:
            self.dfs(p+'(', n, ps, ocount+1, ccount)
        if ccount< ocount:
            self.dfs(p+')', n, ps, ocount, ccount+1)
    
    
                
        
        
        
        