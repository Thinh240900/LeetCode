class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        # Deal with 0
        if numerator == 0:
            return '0'

        result = []

        # Deal with negative numbers
        if numerator < 0:
            if denominator < 0:
                denominator = -denominator
            else:
                result.append('-')
            numerator = -numerator
        else:
            if denominator < 0:
                result.append('-')
                denominator = -denominator

        # upper part
        result.append(str(numerator // denominator))
        numerator %= denominator

        # check if no decimal part
        if numerator == 0:
            return ''.join(result)

        # lower part
        result.append('.')
        check_exist_index = {}
        while numerator!= 0:
            if numerator in check_exist_index:
                result.insert(check_exist_index[numerator], '(')
                result.append(')')
                break
            else:
                check_exist_index[numerator] = len(result)

            numerator *= 10
            result.append(str(numerator // denominator))
            numerator %= denominator

        return ''.join(result)

print(Solution().fractionToDecimal(1, 2)) # "0.5"
print(Solution().fractionToDecimal(2, 1)) # "2"
print(Solution().fractionToDecimal(2, 7))
print(Solution().fractionToDecimal(4, 333)) # "0.(012)"
