class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # l, r = 0, len(s)-1
        # while l < r:
        #     s[l], s[r] = s[r], s[l]
        #     l += 1
        #     r -= 1
        self.reverse(s, 0, len(s)-1)
    
    def reverse(self, s, start, end):
        if start > end:
            return
        s[start], s[end] = s[end], s[start]
        self.reverse(s, start + 1, end - 1)
      
        