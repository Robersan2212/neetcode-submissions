class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Check if both strings have the same length, if they don't they are not anagrams
        if len(s) != len(t):
            return False

        #Create both hashmaps
        countS, countT = {}, {}

        #iterate through the indeces of both strings to update hashmaps in each pass
        for i in range(len(s)):
            #update each hasmap with current character in the string
            countS[s[i]] = countS.get(s[i], 0) + 1
            countT[t[i]] = countT.get(t[i], 0) + 1
        # return true if both hashmaps are the same
        return countS == countT