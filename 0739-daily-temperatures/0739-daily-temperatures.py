class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = []
        ans = [0]*len(temperatures)
        for cur_day, cur_temp in enumerate(temperatures):
            
            while st and temperatures[st[-1]] < cur_temp:
                pre = st.pop()
                ans[pre] = cur_day - pre
            
            st.append(cur_day)
        return ans
                
                
        
        