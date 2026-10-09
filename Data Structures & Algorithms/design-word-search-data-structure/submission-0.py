class WordDictionary:
    class TrieNode:
        def __init__(self, val=0, kids=None,end=None):
            self.val = val
            self.kids = kids if kids is not None else [None]*26
            self.end = False

    def __init__(self):
        self.root = self.TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for i in range(len(word)):
            char = word[i]
            numChar = ord(char)-ord('a')
            if not curr.kids[numChar]:
                curr.kids[numChar] = self.TrieNode(char)
            curr = curr.kids[numChar]
        curr.end = True

    def search(self, word: str) -> bool:
        curr = self.root
        
        def helper(curr, word):
            for i in range(len(word)):
                char = word[i]
                numChar = ord(char)-ord('a')
                if char != ".":
                    if curr.kids[numChar] == None:
                        return False
                    curr = curr.kids[numChar]
                else:
                    for kid in curr.kids:
                        if not kid:
                            continue
                        tempAns = helper(kid, word[i+1:])
                        if tempAns:
                            return True
                    return False
            return curr.end
        
        return helper(curr, word)
