class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        # Given a string s consisting of words and spaces, return the length of the last word in the string input s.
        # traverse the string from right to left, set a boolean flag when encountering non-whitespace character, start the integer counter then
        # continue traversing until a whitespace is found, return the counter

        # Initialize the counter and the flag
        counter, flag = 0, False

        # Traverse the string from right to left
        for i in range(len(s) - 1, -1, -1):
            if s[i] != ' ':
                counter += 1
                flag = True
            elif flag and s[i] == ' ':
                return counter

        return counter
