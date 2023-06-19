class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        ans_set = set()
        
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            
            
            target = -nums[i]
            f = i+1
            e = len(nums)-1
            while f < e:
                if nums[f]+nums[e] == target:
                    new_ans = (nums[i], nums[f], nums[e])
                    if new_ans not in ans_set:
                        ans_set.add(new_ans)
                        ans.append([nums[i], nums[f], nums[e]])
                    f += 1
                    e -= 1
                    continue

                if nums[f]+nums[e] < target:
                    f += 1
                    continue
                else:
                    e -= 1
                    
        return ans
                    
