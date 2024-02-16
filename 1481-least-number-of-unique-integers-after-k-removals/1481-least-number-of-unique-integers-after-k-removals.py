class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        d = Counter(arr)
        for num, count in sorted(d.items(), key=lambda item: item[1]):
            while k > 0 and count > 0:
                k -= 1
                count -= 1
                if count == 0:
                    del d[num]
            if k < 0:
                break
        return len(d)
                    
            
                        
        