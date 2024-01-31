class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        self.helper(0, n, '', ans)
        return ans
    
    def helper(self, left, n, cur, ans):
        if len(cur) == 2*n:
            if left==0:
                ans.append(cur)
            return
        # if start > 2*n:
        #     return
        if left > 0:
            # +left
            self.helper(left+1, n, cur+'(', ans)
            # +right
            self.helper(left-1, n, cur+')', ans)
        
        else:
            self.helper(left+1, n, cur+'(', ans)
            
            
      
       
            
        
        
        
        
        