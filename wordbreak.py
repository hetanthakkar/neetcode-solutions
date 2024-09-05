def partition(s, wordDict):
    state = []
    solution = []
    dictionary = set(wordDict)

    memo1 = {}

    def get_candidates(current):
        sub_index = []
        for i in range(current, len(s)):
            sub_index.append(i)
        return sub_index

    def check_palindrome(start, end):

        if s[start : end + 1] in dictionary:
            return True
        return False

    def search(current):

        if current in memo1:
            return memo1[current]

        nonlocal state

        if current == len(s):
            memo1[current] = True
            return True

        for candidate in get_candidates(current):
            if check_palindrome(current, candidate):
                state.append(s[current : candidate + 1])
                temp = search(candidate + 1)
                state.pop()
                if temp == True:
                    memo1[current] = temp
                    return temp

        memo1[current] = False
        return False

    return search(0)


print(partition("aaaaaaa", ["aaaa", "aaa"]))
