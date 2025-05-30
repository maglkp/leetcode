import math


def myAtoi(s: str) -> int:
    if len(s) == 0:
        return 0

    s_list = list(s)
    i = 0
    while i < len(s_list) and is_white(s_list[i]):
        i += 1

    j = i + 1
    while j < len(s_list) and is_digit(s_list[j]):
        j += 1
    j -= 1

    # single char string
    # no digit or sign found
    # sign not followed by digit
    if i > len(s_list) - 1 or \
            not is_digit_or_sign(s_list[i]) or \
            not is_digit(s_list[j]):
        return 0

    negative_multiplier = 1
    if is_sign(s_list[i]):
        if ord(s_list[i]) == 45:
            negative_multiplier = -1
        num_str = s_list[i + 1:j + 1]
    else:
        num_str = s_list[i:j + 1]

    # remove leading 0s
    i = 0
    while i < len(num_str) and ord(num_str[i]) == 48:
        i += 1
    num_str = num_str[i:]

    if negative_multiplier == 1 and is_larger(''.join(num_str), "2147483647"):
        return 2147483647
    if negative_multiplier == -1 and is_larger(''.join(num_str), "2147483648"):
        return -2147483648

    num_str.reverse()
    num = 0
    for i in range(len(num_str)):
        num += int(math.pow(10, i)) * (ord(num_str[i]) - 48)
    return num * negative_multiplier


def is_sign(c) -> bool:
    # 43 +
    # 45 -
    return ord(c) == 43 or ord(c) == 45


def is_white(c) -> bool:
    return ord(c) == 32


def is_digit_or_sign(c) -> bool:
    return is_digit(c) or is_sign(c)


def is_digit(c) -> bool:
    return 48 <= ord(c) <= 57


def is_larger(x: str, y: str) -> bool:
    if len(x) != len(y):
        return len(x) > len(y)
    for i in range(len(x)):
        if int(x[i]) != int(y[i]):
            return int(x[i]) > int(y[i])
    return False


print(myAtoi("-"))
print(myAtoi("- 1"))
print(myAtoi("x"))
print(myAtoi("1"))
print(myAtoi("1-"))
print(myAtoi("1 -"))
print(myAtoi("+1"))
print(myAtoi("+1 -"))
print(myAtoi("-15"))
print(myAtoi("15"))
print(myAtoi("2147483648"))
print(myAtoi("-2147483648"))
print(myAtoi("leading 5"))
print(myAtoi("5 trailing"))
print(myAtoi("  0000000000012345678"))
