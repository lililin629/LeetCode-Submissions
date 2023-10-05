class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        st = []
        intervals.sort()
        st.append(intervals[0][0]) 
        st.append(intervals[0][1])
        
        for i in range(1, len(intervals)):
            pre = st.pop()
            next_start = intervals[i][0]
            next_end = intervals[i][1]
            
            if next_end <= pre:
                st.append(pre)
            elif next_start <= pre:
                st.append(next_end)
            else:
                st.append(pre)
                st.append(next_start)
                st.append(next_end)
        ans = []
        for i in range(0, len(st), 2):
            ans.append([st[i], st[i+1]])
        return ans
            
            
                
                
        
        
            
        