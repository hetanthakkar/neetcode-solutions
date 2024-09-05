class TrieNode:
    def __init__(self, char=None, isEnd=0):
        self.children = [None for _ in range(26)]
        self.wordEnd = isEnd
        self.char = char
        self.number_of_words = 1


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

    def collect_all_words(self):
        words = []

        def recurse_collect(node, path):
            if node.wordEnd:
                for i in range(node.number_of_words):
                    words.append("".join(path))
            for i, child in enumerate(node.children):
                if child:
                    path.append(chr(i + ord("a")))
                    recurse_collect(child, path)
                    path.pop()

        recurse_collect(self.root, [])
        return words


wordDictionary = Trie()
wordDictionary.insert("aaa")
print(wordDictionary.collect_all_words())
# print(wordDictionary.search("b.."))
print("dkfn")

["a", "b", "c", "e"],
["x", "x", "c", "d"],
["x", "x", "b", "a"]
