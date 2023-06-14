# https://leetcode.com/problems/implement-trie-prefix-tree

class TrieNode():
    def __init__(self):
        self.data = {}
        # be careful with is_word_end assignment and check
        self.is_word_end = False
    
    def add(self, s: str, index: int) -> None:
        if index < len(s):
            ch = s[index]
            if ch not in self.data:
                self.data[ch] = TrieNode()
            if index + 1 == len(s):
                self.data[ch].is_word_end = True
            else:
                self.data[ch].add(s, index + 1)

    def contains(self, s: str, index: int, isSearch: bool) -> bool:
        if index < len(s):
            ch = s[index]
            if ch not in self.data:
                return False
            if index + 1 == len(s):
                if not isSearch:
                    return True
                else:
                    return self.data[ch].is_word_end
            return self.data[ch].contains(s, index + 1, isSearch)

class Trie:
    def __init__(self):
        self.root = TrieNode()        

    def insert(self, word: str) -> None:
        self.root.add(word, 0)

    def search(self, word: str) -> bool:
        return self.root.contains(word, 0, True)

    def startsWith(self, prefix: str) -> bool:
        return self.root.contains(prefix, 0, False)