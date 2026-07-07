class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #check if the lenght of the string are the same
        if len(s) != len(t):
            return False
        
        #create two hasmaps to keep track of the character frequency count
        countS, countT = {}, {}

        #iterate through each indeces of each character of both strings so in each pass both
        #hashmaps update
        for i in range(len(s)):
            #update both hashmaps:
            countS[s[i]] = countS.get(s[i], 0) + 1
            countT[t[i]] = countT.get(t[i],0) + 1
        return countS == countT