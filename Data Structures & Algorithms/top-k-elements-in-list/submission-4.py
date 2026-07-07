class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #hashmap to keep track of frequencies
        hashmap = {}
        #buckets to sort different frequencies values whe frequencies are indexes
        freq = [[] for i in range(len(nums)+1)]

        #keep count of frequencies with hashmap
        for n in nums:
            hashmap[n] = hashmap.get(n, 0) +1
        for n,c in hashmap.items():
            freq[c].append(n)
        
        #add numbers to result list
        res = []
        #start a walkthough backwards to check buckets
        for n in range(len(freq) -1, 0, -1 ):
            for n in freq[n]:
                res.append(n)
                if len(res) == k:
                    return res

            