class TrieNode:
    def __init__(self, char=None, isEnd=0):
        self.children = [None for _ in range(26)]
        self.wordEnd = isEnd
        self.char = char


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode(None, False)

    def insert(self, word):
        start = self.root

        def recurse_insert(i, start):
            if i == len(word):
                if start.wordEnd:
                    start.number_of_words += (
                        1  # Increment word count if the word already exists
                    )
                start.wordEnd = True  # Ensure wordEnd is set when inserting a new word
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
    trie = Trie()
    height = len(board)
    width = len(board[0])
    seen = set()
    state = []
    letters = set()
    for w in word:
        letters.add(w[0])

    def get_candidates(i, j, seen):
        neighbor = []
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < height and 0 <= nj < width:
                if tuple([ni, nj]) not in seen:
                    neighbor.append(tuple([ni, nj]))
        return neighbor

    def search(i, j, current):
        found = False
        # if current == len(word):
        #     return True

        for candidate in get_candidates(i, j, seen):

            # if current > len(word) - 1:
            #     return False
            if board[candidate[0]][candidate[1]]:
                state.append(board[candidate[0]][candidate[1]])
                char = ""
                for c in state:
                    char += c
                trie.insert(char)
                seen.add((candidate[0], candidate[1]))
                found = search(candidate[0], candidate[1], current + 1)
                # if found:
                #     return True
                seen.remove((candidate[0], candidate[1]))
                state.pop()
        return found

    for row in range(height):
        for col in range(width):
            if board[row][col] in letters:
                result = search(row, col, 0)
                seen = set()
                # if result:
                #     return True
                seen.clear()
                state = []
    ans = []
    for word in word:
        if trie.search(word):
            ans.append(word)
    return ans


board = [["a", "a"]]
word = "aa"
print(exist(board, word))
