from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        trie = self.Trie()
        trie.insert_all(words)

        # change this to dict with value = num of occurrences
        words = set(words)
        words_to_be_found = set(words)
        root_ix = 0
        ix = 0
        solutions = []
        prefix_acc = ""

        while ix < len(s):
            reset = False
            word_candidate = prefix_acc + s[ix]
            if not trie.any_starts_with(word_candidate):
                reset = True
            elif trie.contains(word_candidate):
                if word_candidate not in words_to_be_found:
                    reset = True
                elif len(words_to_be_found) == 1:
                    solutions.append(root_ix)
                    ix += 1
                    root_ix = ix
                    words_to_be_found = set(words)
                    prefix_acc = ""
                else:
                    words_to_be_found.remove(word_candidate)
                    prefix_acc = ""
                    ix += 1
            else:
                prefix_acc += s[ix]
                ix += 1

            if reset:
                root_ix += 1
                ix = root_ix
                words_to_be_found = set(words)
                prefix_acc = ""

        return solutions

    class Trie:
        def __init__(self):
            self.node = {}

        def insert_all(self, words: List[str]):
            for word in words:
                self.insert(word)

        def insert(self, word: str):
            current_node = self.node
            for c in word:
                if c not in current_node:
                    current_node[c] = {}
                current_node = current_node[c]
            current_node["is_real_word"] = True

        def contains(self, word):
            current_node = self.node
            for c in word:
                if c not in current_node:
                    return False
                current_node = current_node[c]
            return "is_real_word" in current_node

        def any_starts_with(self, prefix):
            current_node = self.node
            for c in prefix:
                if c not in current_node:
                    return False
                current_node = current_node[c]
            return True


# t = Solution.Trie()
# t.insert("ab")
# t.insert("a")
# t.insert("apple")
# print(t.any_starts_with("ab"))
# print(t.any_starts_with("a"))
# print(t.any_starts_with("app"))
# print(t.any_starts_with("apple"))

#s = "barfoothefoobarman"
#words = ["foo", "bar"]
s = "wordgoodgoodgoodbestword"
words = ["word","good","best","word"]

sol = Solution()
ixs = sol.findSubstring(s, words)
print(ixs)
