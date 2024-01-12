class Solution:
    def longestValidParentheses(self, s: str) -> int:
        dp = [0 for _ in range(len(s))]
        maxlen = 0
        for i in range(1, len(s)):
            if s[i] == ')':
                if s[i - 1] == '(':
                    if i >= 2:
                        offset = dp[i - 2]
                    else:
                        offset = 0
                    dp[i] = offset + 2
                #  s[i - 1] == ')'
                elif i - dp[i - 1] -1 >= 0 and s[i - dp[i - 1] - 1] == '(':
                    if i - dp[i - 1] - 2 >= 0:
                        offset = dp[i - dp[i - 1] - 2]
                    else:
                        offset = 0
                    dp[i] = dp[i - 1] + offset + 2
            maxlen = max(maxlen, dp[i])

        return maxlen

    def longestValidParenthesesWindow(self, s: str) -> int:
        if len(s) == 1:
            return 0

        # init left and right indexes
        left, right = 0, 0
        # init number of currently open parentheses that are not closed
        open_count = 0
        current_longest_left, current_longest_right = 0, 0

        while right < len(s):
            # if current char is open parentheses, increase open count
            if s[right] == '(':
                open_count += 1
                right += 1
            # if current char is closed parentheses, decrease open count
            # or reset window and save the window if open count is 0
            elif s[right] == ')':
                if open_count > 0:
                    open_count -= 1
                    right += 1
                else:
                    # compare it against current and only update if it's longer
                    prev_right = right - 1
                    if prev_right - left > current_longest_right - current_longest_left:
                        current_longest_left, current_longest_right = left, prev_right
                    left = right + 1
                    right = left

        # cant override here, need to contract first
        prev_right = right - 1
        if prev_right - left > current_longest_right - current_longest_left:
            current_longest_left, current_longest_right = left, prev_right

        if open_count > 0:
            reverse_open_count = 0
            left = len(s) - 1
            while left >= 0:
                # if current char is reverse-open parentheses, increase open count
                if s[left] == ')':
                    reverse_open_count += 1
                    left -= 1
                # if current char is reverse-closed parentheses, decrease open count
                elif s[left] == '(':
                    if reverse_open_count > 0:
                        reverse_open_count -= 1
                        left -= 1
                    else:
                        break

            return len(s[left + 1:])

        return len(s[current_longest_left:current_longest_right + 1])


s = Solution()
v = "(()"
v = ""
v = ")()())"
v = "()"
v = "((((()"
v = "()(()"
v = ")()())()()("
v = ")()())()(((("
v = "()(())"
v = ")()())"
print(s.longestValidParentheses(v))
