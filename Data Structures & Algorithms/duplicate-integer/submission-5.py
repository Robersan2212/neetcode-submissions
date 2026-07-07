class Solution:
    #Hashset approach where every value gets compared to the hashset. If the value has not been seen in the 
    #hashset, it gets stored until duplicates are found to return "true" or none and "False" gets returned
    def hasDuplicate(self, nums: List[int]) -> bool:
        #Initialize hashset
        hashset = set()

        #Iterate through every value in the the array
        for num in nums: 
            #check if current number is in hashset and return true
            if num in hashset:
                return True
            #If not seen, number gets stored in hashset
            hashset.add(num)
        # If none of the conditions in the previous loop are true, return "False"
        return False