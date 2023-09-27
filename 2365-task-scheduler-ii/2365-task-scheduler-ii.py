class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        d = defaultdict(int) # {task: lastday, }
        d[tasks[0]] = 1
        today = 1
        
        for i in range(1, len(tasks)):
            # print(d)
            if tasks[i] in d:
                if today-d[tasks[i]] <= space:
                    today += (space-today+d[tasks[i]]+1) 
                else:
                    today += 1
            else:
                today += 1
            d[tasks[i]] = today
        
        return today
            
        
        