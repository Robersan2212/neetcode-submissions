class Solution:
    def isPalindrome(self, s: str) -> bool:
        #two pointer on opposite ends
        l, r = 0, len(s) -1

        #two pointer guardrail to prevent cross pointers l<r
        while l < r:
            #filter non-alphanumeric char
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            #compare valid indeces with valid char lowercase
            if s[l].lower() != s[r].lower(): 
                return False
            # move pointers when both characters are the same. 
            l += 1
            r -= 1
        return True
            