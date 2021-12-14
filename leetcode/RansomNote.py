# Leetcode
# 383. Ransom Note
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(magazine) < len(ransomNote):
            return False
        
        mag_counter = collections.Counter(magazine)
        ransom_counter = collections.Counter(ransomNote)
        
        for alpha in ransom_counter:
            if ransom_counter.get(alpha, -1) > mag_counter.get(alpha, 0):
                return False
        return True
    
####################################################################    
#         #Alternate solution            
#         counter = collections.Counter(magazine)
#         ransomNote = list(ransomNote)
        
#         for alpha in list(ransomNote):
#             ransomNote.remove(alpha)
#             alpha_count = counter.get(alpha, -1)
#             if alpha_count > 1:
#                 counter[alpha] = counter.get(alpha) - 1 
#             elif alpha_count == 1:
#                 counter.pop(alpha)
#             else:
#                 return False
            
#         if not ransomNote:
#             return True
#         else:
#             return False
            