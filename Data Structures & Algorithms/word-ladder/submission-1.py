class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        count = 0
        q = deque()
        q.append(beginWord)
        visited = set()

        while q:
            count += 1
            for _ in range(len(q)):
                cur = q.popleft()
                for i in range(len(cur)):
                    tmp = cur[:i] + cur[i+1:]
                    for word in wordList:
                        tmp2 = word[:i] + word[i+1:]
                        if tmp == tmp2 and word not in visited:
                            if word == endWord:
                                return count + 1
                            q.append(word) 
                            visited.add(word)
        
        return 0