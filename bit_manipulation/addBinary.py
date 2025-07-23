class Solution:
    def addBinary(self, a: str, b: str) -> str:
        b_r = list(reversed(b))
        a_r = list(reversed(a))

        n = max(len(b_r), len(a_r))
        carry = False
        result = []
        for i in range(n):
            ai = a_r[i] if i < len(a_r) else "0"
            bi = b_r[i] if i < len(b_r) else "0"
            if ai == "1" and bi == "1":
                result.append("1" if carry else "0")
                carry = True
            elif ai == "0" and bi == "0":
                result.append("1" if carry else "0")
                carry = False
            else:
                result.append("0" if carry else "1")

        if carry:
            result.append("1")


        return "".join(reversed(result))




a = "1010"
b = "1011"
a = "11"
b = "1"
s = Solution()
print(s.addBinary(a, b))