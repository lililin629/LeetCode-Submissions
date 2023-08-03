class TimeMap:

    def __init__(self):
        # {key:[(time, val), (time, val), ...], }
        self.d = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        lst = self.d[key]
        if not lst:
            return ""
        l = 0
        r = len(lst) - 1
        while l + 1 < r:
            m = (l+r)//2
            if lst[m][0] == timestamp:
                return lst[m][1]
            elif lst[m][0] < timestamp:
                l = m
            else:
                r = m
        if lst[r][0] <= timestamp:
            return lst[r][1] 
        if lst[l][0] <= timestamp:
            return lst[l][1] 

        return ""



        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)