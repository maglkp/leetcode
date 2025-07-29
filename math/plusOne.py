from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            digit = digits[i] + carry
            if digit > 9:
                carry = 1
                digit = 0
            else:
                carry = 0
            digits[i] = digit

        if carry:
            digits.insert(0, 1)
        return digits


