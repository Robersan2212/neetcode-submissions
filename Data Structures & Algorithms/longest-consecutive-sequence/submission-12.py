class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #hashset to store all unique numbers from the array
        hash_set = set()
        #variable to keep track of the longest sequence count
        longest = 0
        #build hashset
        for num in nums:
            hash_set.add(num)
        #iterate through the hashset
        for num in hash_set:
            #find the sequence by lokking for the start number x - 1
            if num - 1 not in hash_set:
                #keep track of length of sequence
                length = 1
                #keep track of current number in the sequence
                current = num
                #look for next number in the sequence
                while current + 1 in hash_set:
                    #length increments
                    length += 1
                    #move to the next number
                    current += 1
                #compare current sequence length to the longest sequence
                if length > longest:
                    longest = length
        #return longest sequence
        return longest