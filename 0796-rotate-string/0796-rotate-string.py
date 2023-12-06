class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        
        cuts = []
        for i in range(len(goal)):
            if goal[i] == s[0]:
                cuts.append(i)
        for cut in cuts:
            l = len(goal) - cut
            if goal[cut:] == s[:l] and goal[:cut] == s[l:]:
                return True
        return False
                
            
        