class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        n = len(nums)
        new = [int(num) for num in nums]
        heapq.heapify(new)
        for i in range(n-k+1):
            cur = heapq.heappop(new)
        return str(cur)
        