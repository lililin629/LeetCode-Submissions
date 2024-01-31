class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        self.helper(0, 0, n, '', ans)
        return ans
    
    def helper(self, start, left, n, cur, ans):
        if len(cur) == 2*n and left==0:
            ans.append(cur)
        if start > 2*n:
            return
        if left > 0:
            # +left
            self.helper(start+1, left+1, n, cur+'(', ans)
            # +right
            self.helper(start+1, left-1, n, cur+')', ans)
        
        else:
            self.helper(start+1, left+1, n, cur+'(', ans)
            
            
      
       
            
        
        
        
        
        