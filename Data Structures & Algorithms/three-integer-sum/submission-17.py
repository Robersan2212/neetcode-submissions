class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # result container
        res = []
        nums.sort()

        #first fixed pointer i
        for i in range(len(nums)):
            l, r = i+1, len(nums)-1

            #check to see if nums[i] is > 0
            if nums[i] > 0:
                break
            
            #check for the duplicate
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            # condition for l and r to not cross while checking.
            while l < r:
                sum = nums[i] + nums[l] + nums[r]
                if sum == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
                elif sum < 0:
                    l += 1
                else:
                    r -= 1

        return res

