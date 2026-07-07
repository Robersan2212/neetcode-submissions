class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        #create a hashset 
        hashset = set()

        #iterate through the array and store the number if not seen in the hashset
        for n in nums:
            if n in hashset:
                return True
            else:
                hashset.add(n)
        return False