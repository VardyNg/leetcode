import math

class Solution:
    def intToRoman(self, num: int) -> str:
        # use hashmap to store symbol and value
        table = {
            "0": "",
            "1": "I",
            "2": "II",
            "3": "III",
            "4": "IV",
            "5": "V",
            "6": "VI",
            "7": "VII",
            "8": "VIII",
            "9": "IX",
            "10": "X",
            "20": "XX",
            "30": "XXX",
            "40": "XL",
            "50": "L",
            "60": "LX",
            "70": "LXX",
            "80": "LXXX",
            "90": "XC",
            "100": "C",
            "200": "CC",
            "300": "CCC",
            "400": "CD",
            "500": "D",
            "600": "DC",
            "700": "DCC",
            "800": "DCCC",
            "900": "CM",
            "1000": "M",
            "2000": "MM",
            "3000": "MMM",
        }

        num_length = int(math.log10(num))+1

        res = ""

        # loop through each digit in num
        # use the value and check the table to get the roman symbols
        for digit, val in enumerate(str(num)):
            digit_val = int(val) * (10 ** (num_length - digit - 1))
            res += table[str(digit_val)]
        return res
            