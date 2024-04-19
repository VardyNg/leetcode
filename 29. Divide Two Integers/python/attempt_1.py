class Solution:
    

    def divide(self, dividend: int, divisor: int) -> int:
        def convert_to_positive(num):
            return abs(num)

        def integer_range_limiter(num):
            bit = 32
            ranger = 2 ** (bit - 1)
            upper_limit = ranger - 1
            lower_limit = -ranger
            if num > upper_limit:
                return upper_limit

            if num < lower_limit:
                return lower_limit

            return num

        # if either dividen or divisor is negative (XOR)
        # invert the final quotient, as it will be converted the positive later
        # do not invert for both dividen and divisor being negative
        # as it will produce positive quotient
        invert_quotient = bool(divisor > 0) ^ bool(dividend > 0)

        # Handle base case
        dividend = convert_to_positive(dividend)
        divisor = convert_to_positive(divisor)

        # Handle base case
        # if dividen smaller than divisor, the quotient (x) is 0 < x <= 1 or -1 <= x < 0 and will be truncated to 0
        if dividend < divisor:
            return 0

        quotient = 0
        if divisor == 1:
            quotient = dividend
        else:
            while dividend >= divisor:
                print(dividend)
                dividend = dividend - divisor
                quotient += 1

        if invert_quotient:
            return integer_range_limiter(0 - quotient)

        return integer_range_limiter(quotient)
            