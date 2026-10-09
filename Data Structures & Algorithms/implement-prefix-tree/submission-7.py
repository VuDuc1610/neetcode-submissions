class PrefixTree:

    class TrieNode:
        def __init__(self, val="", kids=None, end=False):
            self.val = val
            self.kids = kids if kids is not None else [None] * 26
            self.end = end

    def __init__(self):
        self.head = self.TrieNode()

    def insert(self, word: str) -> None:
        root = self.head
        for i in range(len(word)):
            char = word[i]
            numChar = ord(char) - ord('a')
            if not root.kids[numChar]:
                root.kids[numChar] = self.TrieNode(char)
            root = root.kids[numChar]
            if i == len(word)-1:
                root.end = True

    def search(self, word: str) -> bool:
        root = self.head
        for i in range(len(word)):
            char = word[i]
            numChar = ord(char)-ord('a')
            if root.kids[numChar] == None:
                return False
            root = root.kids[numChar]

            if i == len(word)-1:
                if root.end == False:
                    return False
        return True

    def startsWith(self, prefix: str) -> bool:
        root = self.head
        for i in range(len(prefix)):
            char = prefix[i]
            numChar = ord(char)-ord('a')

            if root.kids[numChar] == None:
                return False
            root = root.kids[numChar]
        return True
        