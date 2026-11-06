class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        count = 1
        q = deque()
        q.append(beginWord)
        visited = set()

        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                if cur == endWord:
                    return count
                for i in range(len(cur)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        tmp = cur[:i] + c + cur[i+1:]
                        if tmp in wordList and tmp not in visited:
                            q.append(tmp) 
                            visited.add(tmp)
            count += 1
        
        return 0