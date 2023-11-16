class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        n = len(temperatures)
        st = []
        ans = [0]*n
        
        for i in range(n):
            while st and temperatures[i] > st[-1][1]:
                idx, temp = st.pop()
                ans[idx] = i - idx   
            st.append((i,temperatures[i]))
        return ans 
            
            
            
        