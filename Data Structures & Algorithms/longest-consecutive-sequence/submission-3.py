class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Hash-set that stores all unique elements of the array n number of times O(n)
        # Iterate through the array, finding the start of the sequence x-1 not in the hashset
        # Update length variable with current walk until breaks and update longest
        # When new walk starts update length with new count, compare with longest, return biggest
        hash_set = set()
        longest = 0

        for num in nums:
            hash_set.add(num)
        
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
                

