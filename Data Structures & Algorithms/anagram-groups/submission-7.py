class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #Hash map to store a sorted version of the string that can be anagram of other strings (e.g "act"-> "cat")
        hashmap = {}
        #Result sublist to store strings
        res = []

        #iterate through the string
        for i in strs:
            #sort string
            sorted_string = "".join(sorted(i))
            #check if sorted string already exists as a key in the hashmap, if it does add the current string to the list:
            if sorted_string in hashmap:
                hashmap[sorted_string].append(i)
            #If the sorted_string does not exist as a key add it
            else:
                hashmap[sorted_string] = [i]
        for i in hashmap.values():
            res.append(i)
        return res