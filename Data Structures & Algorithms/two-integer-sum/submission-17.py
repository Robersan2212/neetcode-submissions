class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashmap = {}

        #check if complemenatry is in map, if not add it to the hashmap
        for i, n in enumerate(nums):
            comp = target - n
            #check complementary in map
            if comp in hashmap:
                return[hashmap[comp], i]
            hashmap[n] = i
        return[]