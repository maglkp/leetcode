import time


class Solution:

    # divide_with_expand
    def divide(self, dividend: int, divisor: int) -> int:

        if dividend == -2 ** 31 and divisor == -1:
            return 2 ** 31 - 1
        if divisor == -1:
            return -dividend
        if divisor == 1:
            return dividend

        dividend_negative = dividend < 0
        divisor_negative = divisor < 0
        negative = dividend_negative != divisor_negative
        divisor = abs(divisor)
        dividend = abs(dividend)

        result = 0
        while dividend >= divisor:
            i = 0
            while divisor ** i < dividend:
                i += 1
            if divisor ** i > dividend:
                i -= 1

            result += divisor ** (i - 1)
            dividend -= divisor ** i

        if negative:
            return -result
        else:
            return result

    def divide_brute(self, dividend: int, divisor: int) -> int:
        dividend_negative = dividend < 0
        divisor_negative = divisor < 0
        negative = dividend_negative != divisor_negative
        if negative:
            threshold = 2 ** 31 - 1
        else:
            threshold = 2 ** 31
        divisor = abs(divisor)
        dividend = abs(dividend)

        result = 0
        acc = 0
        while acc < dividend:
            acc += divisor
            result += 1

            if result > threshold:
                if negative:
                    return -threshold
                else:
                    return threshold

        if acc > dividend:
            result -= 1
        if negative:
            return -result
        else:
            return result


start_time = time.time()

s = Solution()
dividend = 7
divisor = -3
d = s.divide(dividend, divisor)
print(d)

print("--- %s seconds ---" % (time.time() - start_time))
