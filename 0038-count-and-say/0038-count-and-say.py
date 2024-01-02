class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        else:
            prev = self.countAndSay(n - 1)
            result = ''
            count = 1
            for i in range(len(prev) - 1):
                if prev[i] == prev[i + 1]:
                    count += 1
                else:
                    result += str(count) + prev[i]
                    count = 1
            result += str(count) + prev[-1]  # Handle the last character/group
            return result

# class Solution:
#     def countAndSay(self, n: int) -> str:
#         return self.helper(n)
    
#     def helper(self, n):
#         if n == 1:
#             return '1'
#         prev = self.helper(n-1)
#         count = 1
#         result = ''
#         for i in range(len(prev)-1):
#             if prev[i] == prev[i+1]:
#                 count += 1
#             else:
#                 result += str(count)
#                 result += prev[i]
#                 count = 1
#         return result
                
            
            
        
        
        
        
        

        
