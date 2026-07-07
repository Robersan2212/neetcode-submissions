class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hashmap = {}

        for n in nums:
            #check if n is in nums
            if n in hashmap:
                hashmap[n] = hashmap[n] + 1
            else:
                hashmap[n] = 1
                
        sorted_hash = sorted(hashmap.items(), key=lambda x: x[1], reverse=True)
        return [n for n, count in sorted_hash[:k]]
            