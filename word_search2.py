class TrieNode:
    def __init__(self, char=None, isEnd=0):
        self.children = [None for _ in range(26)]
        self.wordEnd = isEnd
        self.char = char
        self.number_of_words = 1
        self.word = None


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode(None, False)

    def insert(self, word):
        start = self.root

        def recurse_insert(i, start):
            if i == len(word) and start.wordEnd:
                start.number_of_words += 1
            if i == len(word):
                start.wordEnd = True
                start.word = word
                return
            index = ord(word[i]) - ord("a")
            if start.children[index] != None:
                recurse_insert(i + 1, start.children[index])
            else:
                start.children[index] = TrieNode(word[i], False)
                recurse_insert(i + 1, start.children[index])

        recurse_insert(0, start)

    def search(self, word):
        start = self.root

        def recurse_search(i, start):
            if i == len(word):
                return start.wordEnd
            index = ord(word[i]) - ord("a")
            if word[i] == ".":
                for k in range(len(start.children)):
                    if start.children[k] != None:
                        if recurse_search(i + 1, start.children[k]):
                            return True
                return False
            if start.children[index] == None:
                return False
            else:
                return recurse_search(i + 1, start.children[index])

        return recurse_search(0, start)

    def startsWith(self, prefix):
        start = self.root

        def recurse_search(i, start):
            if i == len(prefix):
                return True
            index = ord(prefix[i]) - ord("a")
            if start.children[index] == None:
                return False
            else:
                return recurse_search(i + 1, start.children[index])

        return recurse_search(0, start)


def exist(board, word):
    res = set()
    trie = Trie()
    height = len(board)
    width = len(board[0])
    seen = set()
    state = []
    letters = set()
    for w in word:
        letters.add(w[0])
    for word in word:
        trie.insert(word)

    def get_candidates(i, j, seen):
        neighbor = []
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < height and 0 <= nj < width:
                if tuple([ni, nj]) not in seen:
                    neighbor.append(tuple([ni, nj]))
        return neighbor

    def search(i, j, node):

        if node.wordEnd:
            res.add(node.word)

        for candidate in get_candidates(i, j, seen):
            char = board[candidate[0]][candidate[1]]
            next_node = node.children[ord(char) - ord("a")]
            if next_node:
                seen.add((candidate[0], candidate[1]))
                search(candidate[0], candidate[1], next_node)
                seen.remove((candidate[0], candidate[1]))

    for row in range(height):
        for col in range(width):
            char = board[row][col]
            node = trie.root.children[ord(char) - ord("a")]
            if node:
                seen.add((row, col))
                state.append(char)
                search(row, col, node)
                seen.remove((row, col))
                state.pop()

    return list(res)


board = [["a", "b", "c", "e"], ["x", "x", "c", "d"], ["x", "x", "b", "a"]]
words = ["abc", "abcd"]
print(exist(board, words))
