# if str no conversion is advised get k-th digit with
# L = log(n, 10)
# mod and div...

def isPalindrome(x: int) -> bool:
    s = str(x)
    i = 0
    half_len_ix = int(len(s) / 2)
    last_ix = len(s) - 1
    while i < half_len_ix:
        if s[i] != s[last_ix - i]:
            return False
        i += 1
    return True



