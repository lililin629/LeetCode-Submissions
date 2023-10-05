class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]
        l = self.bi_search(intervals, newInterval[0])
        #if intervals[l][1] >= newInterval[1]: nothing happens
        if l == -1:
            intervals = [newInterval] + intervals
        elif intervals[l][1] < newInterval[1] and intervals[l][1] >= newInterval[0]:
            intervals[l][1] = newInterval[1]
        elif intervals[l][1] < newInterval[0]:
            intervals.append(newInterval)
            intervals.sort()
        
        print(intervals)
        st = [intervals[0][0], intervals[0][1]]
        ans = []
        for i in range(1, len(intervals)):
            pre = st.pop()
            if pre >= intervals[i][1]:
                st.append(pre)
            elif pre >= intervals[i][0]:
                st.append(intervals[i][1])
            else:
                st.append(pre)
                st.append(intervals[i][0])
                st.append(intervals[i][1])
        for i in range(0,len(st), 2):
            ans.append([st[i], st[i+1]])
        return ans
            
            
        
            
            
            
            
      
    
    # returns indices of left and right interval
    def bi_search(self, intervals, target): 
        
        l = 0
        r = len(intervals)-1
        while l + 1 < r:
            m = (l+r)//2
            if intervals[m][0] > target:
                r = m
            else:
                l = m
        if intervals[l][0] > target:
            return -1
        return l
                
            
        
        