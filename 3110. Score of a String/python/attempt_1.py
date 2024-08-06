class Solution:
    def scoreOfString(self, s: str) -> int:
        
        # set the pointer to at index 1, as the string length >= 2
        pointer = 1
        score = 0

        # loop from s[1] to the last character
        # get and add the absolute value of s[pointer - 1] - s[pointer] 
        while pointer < len(s):
            score += abs(ord(s[pointer - 1]) - ord(s[pointer]))
            pointer += 1

        return score
