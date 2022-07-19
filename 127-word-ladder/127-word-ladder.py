import collections
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        new_dict = collections.defaultdict(list)
        l = len(endWord)
        for word in wordList:
            for i in range(l):
                new_dict[word[:i] + "*" + word[i+1:]].append(word)
        # BFS
        queue = collections.deque([(beginWord, 1)])
        visited = []
        while queue:
            cur_word, level = queue.popleft()
            for i in range(l):
                look_up_word = cur_word[:i] + "*" + cur_word[i+1:]
                for word in new_dict[look_up_word]:
                    if word == endWord:
                        return level + 1
                    if word not in visited:
                        visited.append(word)
                        queue.append((word, level+1))
                new_dict[look_up_word] = []
        return 0