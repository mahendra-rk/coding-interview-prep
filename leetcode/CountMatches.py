#LeetCode 
#1773. Count Items Matching a Rule

class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        index = 0
        match = 0
        if ruleKey == "color":
            index = 1
        elif ruleKey == "name":
            index = 2
        for item in items:
            if item[index] == ruleValue:
                match += 1
        return match
            