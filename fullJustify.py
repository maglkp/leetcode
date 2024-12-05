from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:

        # loop until there are no more words
        start_ix = 0
        end_ix = 0
        justified: List[str] = []
        while start_ix < len(words):
            # add words until they don't fit the maxWidth including one space between them
            while end_ix < len(words) and not self.would_go_over_max_width(words[start_ix:end_ix + 1], maxWidth):
                end_ix += 1

            current_line_to_justify = words[start_ix:end_ix]
            is_last_line = end_ix == len(words)
            if is_last_line:
                space_needed = maxWidth - sum(map(lambda a: len(a), current_line_to_justify)) - (len(current_line_to_justify) - 1)
                justified.append(" ".join(current_line_to_justify) + " " * space_needed)
            else:
                # calculate how much space is needed for padding
                space_needed = maxWidth - sum(map(lambda a: len(a), current_line_to_justify))
                # distribute the space between the words
                whitespace_distribution = self.distribute_integer(space_needed, len(current_line_to_justify) - 1)
                whitespace = list(map(lambda a: " " * a, whitespace_distribution)) + [""]  # drop list()?

                # distribute the space between the words according to requirements zipping with whitespace
                justified.append("".join(map(lambda a: a[0] + a[1], zip(current_line_to_justify, whitespace))))

            ## if it's the last line it should be left-justified
            start_ix = end_ix

        return justified

    def would_go_over_max_width(self, words: List[str], maxWidth: int) -> bool:
        return sum(map(lambda a: len(a), words)) + len(words) - 1 > maxWidth

    # distribute an integer into integer values as equally as possible
    # where values on the left get larger values if necessary
    def distribute_integer(self, x, n):
        if n == 0:
            return [x]
        if x == 0:
            return [0]

        quotient = x // n
        remainder = x % n
        result = [quotient] * n

        for i in range(remainder):
            result[i] += 1

        return result


words = ["This", "is", "an", "example", "of", "text", "justification."]
words = ["What", "must", "be", "acknowledgment", "shall", "be"]
maxWidth = 16
s = Solution()
j = s.fullJustify(words, maxWidth)
for line in j:
    print(line + '#')
