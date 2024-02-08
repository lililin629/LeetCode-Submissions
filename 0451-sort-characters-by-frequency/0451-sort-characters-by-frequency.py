class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        lst = [(ct, ch) for (ch,ct) in count.items()]
        lst.sort(reverse= True)
        ans = ''
        for (ct, ch) in lst:
            ans += ct*ch
        return ans
            
        
# class Solution:
#     def frequencySort(self, s: str) -> str:
#         count = Counter(s)
#         lst = [(ct, ch) for (ch,ct) in count.items()]
        
#         n = len(lst)
#         self.qs(0, n-1, lst)
#         ans = ''
#         for (ct, ch) in lst[::-1]:
#             ans += ch*ct
#         return ans
    
#     def qs(self, start, end, lst):
#         if start >= end:
#             return
#         l, r = start, end
#         piv = lst[(l+r)//2]
#         while l <= r:
#             while l <= r and lst[r] > piv:
#                 r -= 1
#             while l <= r and lst[l] < piv:
#                 l += 1 
            
#             if l <= r:
#                 lst[l], lst[r] = lst[r], lst[l]
#                 r -= 1
#                 l += 1
#         self.qs(start, r, lst)
#         self.qs(l, end, lst)
                
            
            
        
    
        
        