def reverse(x: int) -> int:
    x_str = str(x)
    negative = x_str[0] == '-'
    if negative:
        x_str = x_str[1:]
    x_list = list(x_str)
    x_list.reverse()
    rev_str = ''.join(x_list)
    if is_larger(rev_str, "2147483647"):
        return 0
    if negative:
        rev_str = "-" + rev_str
    return int(rev_str)


def is_larger(x: str, y: str) -> bool:
    if len(x) != len(y):
        return len(x) > len(y)
    for i in range(len(x)):
        if int(x[i]) != int(y[i]):
            return int(x[i]) > int(y[i])
    return False

#2143847412
#2147483647
print(reverse(-2147483412))
              #2143847412
print(reverse(2147483648))
print(reverse(-2147483647))
print(reverse(-2147483648))
print(reverse(1))
print(reverse(0))
print(reverse(123))
print(reverse(-123))
