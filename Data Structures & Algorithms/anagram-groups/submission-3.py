class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #Create a hashmap with a default list to prevent a KeyError
        hashmap = defaultdict(list)

        #Loop through each string in the array
        for s in strs:
            #sort each string to store the sorted string as a key
            sortedS = ''.join(sorted(s))
            #store sortedS as a key and the string as value
            hashmap[sortedS].append(s)
        return list(hashmap.values())