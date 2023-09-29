class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        d1 = defaultdict(int)
        l = r = 0
        max_len = 0
        total = 0  # To keep the running sum within the window
        
        nums.sort()  # Sort the array to fix the maximum number within the window
        
        while r < len(nums):
            # Increment the count of current number
            d1[nums[r]] += 1
            # Update the running sum within the window
            total += nums[r]
            
            # If the difference between max_num*(r-l+1) and total is greater than k,
            # then shrink the window from the left
            if nums[r] * (r - l + 1) - total > k:
                # Decrease the count of the leftmost number in the window
                d1[nums[l]] -= 1
                # Update the running sum within the window
                total -= nums[l]
                l += 1
                
            # Update the maximum length of the subarray
            max_len = max(max_len, r - l + 1)
            r += 1
            
        return max_len
      