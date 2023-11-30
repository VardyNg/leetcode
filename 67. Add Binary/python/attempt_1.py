class Solution:
    def binaryToDecimal(self, binary_string: str) -> int:
        decimal = 0
        binary_string_length = len(binary_string)
        for idx in range(0, binary_string_length):
            digit = int(binary_string[idx])
            decimal += digit * (2 ** (binary_string_length - idx - 1))
        return decimal

    def decimalToBinary(self, decimal: int) -> str:
        max_exp = 0 # max_exp = length of the result binary
        while True:
            if 2 ** max_exp >= decimal:
                break
            max_exp += 1

        binary = ""
        for exp in range(max_exp, -1, -1):
            val = 2 ** exp
            if decimal >= val:
                binary += "1"
                decimal -= val
            elif binary != "":
                binary += "0"

        if binary == "":
            binary = "0"
        return binary

    def addBinary(self, a: str, b: str) -> str:
        # convert a and b to decimal
        # do the addition
        # convert the result to binary
        
        a = self.binaryToDecimal(Solution, binary_string=a)
        b = self.binaryToDecimal(Solution, binary_string=b)
        
        result = a + b
        return self.decimalToBinary(Solution, decimal=result)
        