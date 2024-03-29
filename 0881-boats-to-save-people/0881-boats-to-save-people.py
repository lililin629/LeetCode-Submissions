class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        n = len(people)
        p1 = n-1
        p2 = 0
        count = 0
        while p1 > p2:
            if people[p1] + people[p2] > limit:
                p1 -= 1 
                count += 1
            else:
                p1 -= 1
                p2 += 1
                count += 1
        if p1 == p2:
            count += 1
        
        return count
        
                
        
        