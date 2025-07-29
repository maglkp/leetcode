class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shift = 0

        while left != right:
            shift += 1
            left >>= 1
            right >>= 1

        return left << shift


    def rangeBitwiseAnd_Linear_Tle(self, left: int, right: int) -> int:
        left_bin = list(bin(left)[2:])
        and_bits = list(map(lambda x: int(x), left_bin))

        for next in range(left + 1, right + 1):
            next_bin = list(bin(next)[2:])

            for i in range(len(and_bits)):
                if next_bin[-(i + 1)] == '0':
                    and_bits[-(i + 1)] = 0
            if sum(and_bits) == 0:
                break

        bits_str = [str(b) for b in and_bits]
        return int("".join(bits_str), 2)


left = 5
right = 7
# left = 1
# right = 2147483647
# left = 600000000
# right = 2147483645
s = Solution()
print(s.rangeBitwiseAnd(left, right))
