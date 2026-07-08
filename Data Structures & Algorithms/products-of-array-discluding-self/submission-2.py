class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # output array
        res = [1] * len(nums)
        # prefix of a product of every element before nums[i]
        prefix = 1
        #iterate through nums to populate prefixes in res on the first pass
        for i in range(len(nums)):
            # res at index i will be equal to the prefix 
            res[i] = prefix
            # prefix will mutiply and update it value according to nums[i]
            prefix *= nums[i]
        # postfix of every element after nums[i]
        postfix = 1
        # iterate through nums from end to beginning on the second pass
        for i in range(len(nums)-1, -1, -1):
            # res will multiply and update its value by multiplying the prefix and post fix
            res[i] *= postfix
            # postfix will multiply with nums[i]
            postfix *= nums[i]
        return res
