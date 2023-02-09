def isMatch(s: str, p: str) -> bool:
    if len(s) == 0 and len(p) > 0:
        return False
    pass


def current_match(s: str, p: list) -> bool:
    s_ix = 0
    for p_ix in range(len(p)):
        pattern_segment = p[p_ix]
        if type(pattern_segment) is tuple and pattern_segment[1] == 0:
            continue

        if s_ix >= len(s):
            return False
        # tuple represents a * with a value of (character or dot, current repetition count)
        # check if it doesn't go beyond the string value
        if type(pattern_segment) is tuple:
            if (pattern_segment[1] - 1) + s_ix > len(s):
                return False
            if pattern_segment[0] != '.' and not all(
                    e == pattern_segment[0] for e in s[s_ix:s_ix + pattern_segment[1]]):
                return False
            s_ix += pattern_segment[1]
        elif pattern_segment == '.' and s_ix < len(s):
            s_ix += 1
        elif s_ix < len(s) and pattern_segment == s[s_ix]:
            s_ix += 1
        #else:
        #    return False

    return s_ix == len(s)


def main_f_loop(s: str, p: list, ix: int):
    pass
    # find ix with *
    # if not found check match
    # expand and call main_f_loop with ix+1
    # if prev call returned false, decrement till 0 and return


def translate_regex_to_single_tokens(s: str) -> list:
    out = []
    i = 0
    while i < len(s):
        if i < len(s) - 1 and s[i + 1] == '*':
            out.append((s[i], 0))
            i += 2
        else:
            out.append(s[i])
            i += 1
    return out


# type(x) is tuple
# print(translate_regex_to_single_tokens(".*"))
# print(translate_regex_to_single_tokens("3*"))
# print(translate_regex_to_single_tokens("."))
# print(translate_regex_to_single_tokens(".*a.a.*"))
# print(translate_regex_to_single_tokens("a*.*"))

# print(current_match("", []))
# print(current_match("abc", ['a', 'b', 'c']))
# print(current_match("abc", ['.', '.', 'c']))
# print(current_match("ab", ['a', 'b', 'c']))
# print(current_match("abc", ['a', 'b']))

print(current_match("abc", [('a', 1), ('b', 1), ('c', 1)]))
print(current_match("abc", [('a', 1), ('b', 1), ('c', 1), ('d', 0)]))
print(current_match("abc", [('.', 1), ('b', 1), ('c', 1)]))
print(current_match("abc", [('.', 2), ('c', 1)]))

print(current_match("abcc", [('.', 2), ('c', 1)]))
print(current_match("abd", [('.', 2), ('c', 1)]))
print(current_match("abc", [('.', 2), ('c', 2)]))
print(current_match("abc", [('.', 2), ('b', 1), ('c', 1)]))
