from typing import List

class Solution:
    def romanToInt(self, s: str) -> int:
        # use hashmap to store symbol and value
        table = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        # we loop from 1st to 2nd last symbol in s
        # then compare the symbol at index against the next symbol (index + 1)
        # if current < next -> minus num by current symbol
        # otherwise, add num by current symbol

        # we initialise num by the last symbol value
        # as the last symbol must be added (positive value)
        num = table[s[-1]]

        # we set the initial val by the 1st symbol
        val = table[s[0]]
        for index in range(0, len(s) - 1):
            # we get the next symbol's value and store in nex_val
            next_val = table[s[index + 1]]
            if val < next_val:
                num -= val
            else:
                num += val

            # assign next_val to val to reduce table look up in next loop
            val = next_val

        return num
        