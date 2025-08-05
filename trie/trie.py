class Trie:

    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        current = self.root
        for c in word:
            if c not in current:
                current[c] = {}
            current = current[c]
        current["is_real_word"] = True

    def search(self, word: str) -> bool:
        current_node = self.root
        for c in word:
            if c not in current_node:
                return False
            current_node = current_node[c]
        return "is_real_word" in current_node

    def startsWith(self, prefix: str) -> bool:
        current_node = self.root
        for c in prefix:
            if c not in current_node:
                return False
            current_node = current_node[c]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)