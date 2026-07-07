class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #create a hashset
        hashset = set()
        
        #iterate through each number in the array
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False