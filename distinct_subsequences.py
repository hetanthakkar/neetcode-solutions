def numDistinct(s, t):
    def search(i, j):
        if j == len(t):
            return 1
        if i == len(s):
            return 0

        # choose
        option1 = 0
        if s[i] == t[j]:
            option1 = search(i + 1, j + 1)

        # not choose
        option2 = search(i + 1, j)
        return option1 + option2

    return search(0, 0)


print(numDistinct("babgbag", "bag"))
