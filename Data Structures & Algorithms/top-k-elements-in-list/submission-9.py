class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #create hashmap where frequencies will be tracked with their corresponding numbers as keys
        hashmap = {}

        #result list to keep track of answers
        res = []

        #iterate through nums and populate hashmap
        for i in nums:
            #check if current number already exists as a key, if it does add 1 to the frequency by 1
            if i in hashmap:
                hashmap[i] += 1
            #if the current number does not exist yet as a key initilize it in the hashmap with a value of 1
            else:
                hashmap[i] = 1
        #initilize bucket array list to keep track of frequencies as indeces and the numbers as values
        bucket_list = [[] for x in range(len(nums) + 1)]
        #iterate through hashmap and populate bucket_list with and index of frequency and a content of the number
        for num, count in hashmap.items():
            bucket_list[count].append(num)
        #iterate through the bucket starting at the end of the array bucket and include the bucket at index 0
        for i in range(len(bucket_list)-1, -1, -1):
            # add all elements from the current bucket to the result list
            res.extend(bucket_list[i])
            #if the length of result is grater or equal to k break out of loop
            if len(res) >= k:
                break
        #return res list wit a slice of index zero to before k 
        return res[:k]





