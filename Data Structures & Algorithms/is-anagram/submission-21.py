class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #compare the length of both strings
        if len(s) != len(t):
            return False
        #create hashmaps
        countS, countT = {}, {}

        #iterate through each character in the string using s for reference
        for i in range(len(s)):
            #keep count of characters in both strings
            countS[s[i]] = countS.get(s[i], 0) + 1
            countT[t[i]] = countT.get(t[i], 0) + 1
        return countS == countT