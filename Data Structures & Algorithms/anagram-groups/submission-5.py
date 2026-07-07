class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #hashmap
        hashmap = {}
        #result list
        res = []
        for i in strs:
            sorted_string = "".join(sorted(i))
            #check if strong is already a key in the hashmap
            if sorted_string in hashmap:
                hashmap[sorted_string].append(i)
            else:
                hashmap[sorted_string] = [i]
        for i in hashmap.values():
            res.append(i)
        return res