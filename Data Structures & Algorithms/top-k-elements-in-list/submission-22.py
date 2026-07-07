class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #hash map with key of number and value of a frequency
        hashmap = {}
        #result list
        res = []

        #iterate through array to populate hashmap
        for i in nums:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
        
        #create an array list
        bucket_list = [[] for x in range(len(nums)+1)]
        #populate bucket list
        for num, count in hashmap.items():
            bucket_list[count].append(num)
        # populate result list
        for i in range(len(bucket_list)-1, -1, -1):
            res += bucket_list[i]
            if len(res) >= k:
                break
        return res[:k]

            