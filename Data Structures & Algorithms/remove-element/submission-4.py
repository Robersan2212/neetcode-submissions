class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #write pointer starts at index 0 (intialize write pointer)
        k = 0

        for i in range (len(nums)) : 
            #i pointer iterates in the array
            if nums[i] != val:
                nums[k] = nums[i]
                #write pointer moves foward
                k += 1
        return k

        