class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #hashmap that takes a key of the number in the array and a value of its count
        hashmap = {}
        #result list
        res = []
        #iterate through array to populate hashmap
        for i in nums:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
        #create bucket list
        bucket_list = [[] for x in range(len(nums)+1)]
        #populate bucket list with frequency as index and number as element
        for num, count in hashmap.items():
            bucket_list[count].append(num)
        #populate res list with most frequent elements. Start iterating bucket list from the last element and start at 0
        for i in range(len(bucket_list)-1, -1, -1):
            res += bucket_list[i]
            #if length of res is >= to k, break out of loop
            if len(res) >= k:
                break
        #return res with a slice of 0 and k to ensure k number of results
        return res[:k]        