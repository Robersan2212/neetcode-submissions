class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        #initialize hashmap
        indices = {}

        #loop to add the numbers with a value of their index
        for i, n in enumerate(nums):
            indices[n] = i
        
        #loop to check for complementary number
        for i, n in enumerate(nums):
            complementary = target - n

            #check if complementary number is in hasmap and != i
            if complementary in indices and indices[complementary] != i:
                return [i, indices[complementary]]

        return[]