class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lst = [nums[0]]
        
        for num in nums[1:]:
            if num > lst[-1]:
                lst.append(num)
            else:
                i = 0
                while lst[i] < num:
                    i += 1
                lst[i] = num
        return len(lst)
                    
                    
            
        
        