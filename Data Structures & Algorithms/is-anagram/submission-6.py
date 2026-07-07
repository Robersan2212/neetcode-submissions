class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Check if both stirngs have the same length
        if len(s) != len(t):
            return False
        
        #Create two hash maps to keep track of the character frequency count
        countS, countT = {}, {}

        #Iterate through each index of each character
        for i in range(len(s)):
            #Update both hasmaps with the caracter count
            countS[s[i]] = countS.get(s[i], 0) + 1
            countT[t[i]] = countT.get(t[i], 0) + 1
        #return true if both hasmaps are the same
        return countS == countT