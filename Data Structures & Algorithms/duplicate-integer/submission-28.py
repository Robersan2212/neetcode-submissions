class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        #initilie set
        hash_set = set()
        #iterate through current values 
        for num in nums:
            #check if value is in hash_set
            if num in hash_set:
                return True
        #add value to hash_set if it does not exist
            hash_set.add(num)
        #return false if all values are unique
        return False
                