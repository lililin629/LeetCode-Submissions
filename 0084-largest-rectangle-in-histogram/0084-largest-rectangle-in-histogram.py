class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # monotonic stack
        st = []
        mx = 0
        for i, h in enumerate(heights):
            start = i
            while st and st[-1][1] > h:
                idx, hi = st.pop()
                mx = max(mx, hi*(i-idx))
                start = idx
            st.append((start, h))
        for i, h in st:
            mx = max(mx, h*(len(heights)-i))
        return mx
                
        # l = 0
        # r = len(heights)-1
        # mxl = 0
        # d = Counter(heights)
        # while l <= r:
        #     h = min(heights[l:r+1])
        #     mxl = max(mxl, h*(r-l+1))
        #     if heights[l] < heights[r]:
        #         d[heights[l]] -= 1
        #         l += 1
        #     else:
        #         d[heights[r]] -= 1
        #         r -= 1
        # return mxl
                
                    
# [4,2,0,3,2,4,3,4]
       
        