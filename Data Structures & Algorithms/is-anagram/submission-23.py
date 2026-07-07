class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        checkCount = {}
        # compare length of both strings
        if len(s) != len(t):
            return False

        #build hashmap from s
        for i in s:
            if i not in checkCount:
                checkCount[i] = 1
            else:
                checkCount[i] += 1
        
        for i in t:
            if i in checkCount:
                checkCount[i] -= 1
            else:
                return False
        
        for i in checkCount:
            if checkCount[i] == 0:
                continue
            else:
                return False
        return True
        
