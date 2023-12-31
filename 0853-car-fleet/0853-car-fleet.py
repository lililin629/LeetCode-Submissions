class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if len (position) == 1:
            return 1
        stk = []
        fleets = 0
        # Pair positions with speeds and sort by position descending
        cars = sorted(zip(position, speed), reverse=True)
        # [(pos1, spd1), (pos2, spd2), ...]
        
        for pos, spd in cars:
            time_to_finish = (target-pos)/spd
            
            if not stk or time_to_finish > stk[-1]:
                fleets += 1
                stk.append(time_to_finish)
        return fleets
      
        
            
                    
                    
                    
                
                
            
            
        
        
        
    
        
        
            
      
        
        