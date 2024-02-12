class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        pat = []
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] > 0:
                pat.append(1)
            elif nums[i] - nums[i-1] == 0:
                pat.append(0)
            elif nums[i] - nums[i-1] < 0:
                pat.append(-1)
            
        length = len(pattern)
       
        
        count = 0
        for j in range(len(pat)-length+1):
            flag = True
            for k in range(length):
                if pat[j+k] != pattern[k]:
                    flag = False
                    break
            if flag:
                count += 1
        
        return count
                    
                
        