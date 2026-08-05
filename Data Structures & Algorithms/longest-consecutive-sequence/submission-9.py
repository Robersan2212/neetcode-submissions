class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_set = set()
        longest = 0
        #build the hash_set with all unique elements
        for num in nums:
            hash_set.add(num)
        #iterate through the hashset to find sequences
        for num in hash_set:
            if num-1 not in hash_set:
                length = 1
                current = num
                while current + 1 in hash_set:
                    length += 1
                    current += 1
                if length > longest:
                    longest = length
        return longest
