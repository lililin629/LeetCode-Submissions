class Solution:
    def binaryGap(self, n: int) -> int:
        flag = False
        first = 0
        shift = 0
        mx_dist = 0
        
        while n != 0:
          
            digi = n % 2
            if digi == 1 and not flag:
                flag = True
                first = shift
                n >>= 1
                shift += 1
                continue
            if digi == 1 and flag:
                mx_dist = max(shift - first, mx_dist) 
                first = shift
                
            n >>= 1
            shift += 1
            
        return mx_dist
           
            
        