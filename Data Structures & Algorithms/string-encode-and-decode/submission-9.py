class Solution:

    def encode(self, strs: List[str]) -> str:
        #initilize encoded string
        res = ""
        #loop through every string in the array
        for s in strs:
            #endcode criteria
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        #initilize decoding array and pointer at the begining of the array
        res, i = [], 0
        #ensure i is in bound
        while i < len(s):
            #initilize j pointer to check for delimeter "#"
            j = i
            #check for delimeter
            while s[j] != "#":
                #move the pointer 1 
                j += 1
            #determine int of number of characters from the string
            length = int(s[i:j])
            #move i pointer after the delimeter
            i = j + 1
            #move j pointer length amount of character
            j = i + length
            #add string to the res array
            res.append(s[i:j])
            #move i to the begining of the next string
            i = j
        return res
