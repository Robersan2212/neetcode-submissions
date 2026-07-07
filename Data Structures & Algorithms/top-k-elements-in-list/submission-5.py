class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #create a hashmap to keep track of the count of frequencies
        count = {}

        #create a collection of buckets that will be equal to the elements in the array
        freq = [[] for n in range(len(nums)+1)]

        #start the count of frequencies in the hashmap
        for n in nums: 
            count[n] = count.get(n, 0) +1
        #assign value to freq buckets 
        for n, c in count.items():
            freq[c].append(n)
        
        #create a result list
        res = []

        #initiate a walkthrough of freq to add to res
        for i in range(len(freq) -1, 0, -1):
            for n in freq[i]:
                res.append(n)
                # check if the len of freq is equal to len of k
                if len(res) == k:
                    return res



            