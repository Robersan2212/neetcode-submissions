class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #chack if both strings have the same length
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}
        
        #iterate through the strins
        for i in range(len(s)):
            countS[s[i]] = countS.get(s[i],0) + 1
            countT[t[i]] = countT.get(t[i],0) + 1
        return countS == countT