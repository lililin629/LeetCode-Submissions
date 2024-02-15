class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        length = len(potions)
        
        # binary search
        ans = [-1]*len(spells)
        for i in range(len(spells)):
            l = 0 
            r = len(potions)-1
            sp = spells[i]
            while l + 1 < r:
                mid = (l + r) // 2
                if sp * potions[mid] < success:
                    l = mid
                else:
                    r = mid
            
            lp = potions[l]
            rp = potions[r]
            
            if sp*lp >= success:
                ans[i] = length - l
            elif sp*rp >= success:
                ans[i] = length - r
            else:
                ans[i] = 0
                
                
        return ans
                
                
                    
            
        