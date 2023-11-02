class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        self.points = defaultdict(int)
        self.memo = defaultdict(int)
        max_number = 0
        # Precompute how many points we gain from taking an element
        for num in nums:
            self.points[num] += num
            max_number = max(max_number, num)
        return self.max_points(max_number)

    
    def max_points(self, num):
        # Check for base cases
        if num == 0:
            return 0
        if num == 1:
            return self.points[1]

        # Apply recurrence relation
        if num not in self.memo:
            self.memo[num] = max(self.max_points(num - 1), self.max_points(num - 2) + self.points[num])
        
        return self.memo[num]
        