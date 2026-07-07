class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #compare if both strings have the same length, if they don't they can't be anagrams
        if len(s) != len(t):
            return False
        
        #create two hashmaps to check the frequency of each character in each string
        countS, countT = {}, {}

        #iterate through each character in the string
        for i in range(len(s)):
            #add each character to the hashmaps with updated value
            countS[s[i]] = countS.get(s[i], 0) + 1
            countT[t[i]] = countT.get(t[i], 0) + 1
        return countS == countT
