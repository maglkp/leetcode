# https://leetcode.com/problems/zigzag-conversion/

def convert(s: str, numRows: int) -> str:
    if len(s) < numRows:
        return s[0:numRows]
    if numRows == 1:
        return s
    r = []

    for rowNum in range(numRows):
        k = rowNum + 1
        r.append(s[rowNum])
        offset_down = 2 * (numRows - k)
        offset_up = 2 * (k - 1)
        ix = rowNum
        if offset_up == 0 and offset_down == 0:
            continue
        while ix < len(s):
            ix += offset_down
            if ix < len(s) and offset_down > 0:
                r.append(s[ix])
            ix += offset_up
            if ix < len(s) and offset_up > 0:
                r.append(s[ix])
    return ''.join(r)

print(convert("ABC", 10))
print(convert("AB", 1))
print(convert("A", 1))
print(convert("PAYPALISHIRING", 3))
# PAHNAPLSIIGYIR

