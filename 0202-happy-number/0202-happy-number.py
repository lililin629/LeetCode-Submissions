class Solution:
    def isHappy(self, n: int) -> bool:
       
        nex = n
        seen = set()
        
        while True:
            sum = 0
            while nex > 0:
                sum += (nex%10)**2
                nex //= 10
            if sum == 1:
                return True
            
            elif sum in seen:
                return False
            
            else:
                seen.add(sum)
                nex = sum
       
            
        