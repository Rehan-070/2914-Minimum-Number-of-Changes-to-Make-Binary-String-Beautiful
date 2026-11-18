# class Solution:
#     def minChanges(self, s: str) -> int:
#         if len(set(s))==1:
#             return 0
        
#         return len(s)//2

class Solution:
    def minChanges(self, s: str) -> int:
        return sum(a != b for a, b in batched(s, 2))
