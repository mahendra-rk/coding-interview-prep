# Leetcode
# 387. First Unique Character in a String
class Solution:
    def firstUniqChar(self, s: str) -> int:
        # counter = collections.Counter(s)
        ####################################################
        counter = {}
        for alphabet in s:
            counter[alphabet] = counter.get(alphabet, 0) + 1
        ####################################################
        for index, alphabet in enumerate(s):
            if counter.get(alphabet) == 1:
                return index
        return -1
