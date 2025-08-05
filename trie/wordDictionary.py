class WordDictionary:

    def __init__(self):
        self.root = {}

    def addWord(self, word: str) -> None:
        current = self.root
        for c in word:
            if c not in current:
                current[c] = {}
            current = current[c]
        current["is_real_word"] = True

    def search(self, word: str) -> bool:
        return self.search_from_node(word, self.root)

    def search_from_node(self, word: str, current_node: dict) -> bool:
        for ix in range(len(word)):
            c = word[ix]
            if c == ".":
                rest = word[ix + 1:]
                for child in current_node:
                    if child == "is_real_word":
                        continue
                    if self.search_from_node(rest, current_node[child]):
                        return True
                return False

            if c not in current_node:
                return False
            current_node = current_node[c]
        return "is_real_word" in current_node

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord("b")
# obj.addWord("bad")
# obj.addWord("dad")
# obj.addWord("mad")
# param_2 = obj.search(".")

obj = WordDictionary()
for w in ["at","and","an","add","bat"]:
    obj.addWord(w)

param_2 = obj.search(".at")

print(param_2)