class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = defaultdict(list)
        for i, num in enumerate(nums):
            d[num].append(i)
                    
        for num in d:
            if target-num in d:
                if target-num == num:
                    if len(d[num]) > 1:
                        return d[num][0:2]
                else:
                    return [d[num][0], d[target-num][0]]
                
       
        
        