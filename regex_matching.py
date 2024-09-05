def isMatch(s, p):

    def search(i, j):
        if i >= len(s) - 1:
            if j <= len(p) - 1:
                if j + 1 < len(p) and (p[j + 1] == "."):
                    return True
                if j + 1 < len(p) and (p[j + 1] == "*"):
                    return search(i, j + 2)
                return False
            if j > len(p) - 1:
                return True
            return True
        if j >= len(p) - 1:
            if i > len(s) - 1:
                return True
            if i < len(s) - 1:
                return False
        if i == len(s) - 1 and j == len(p) - 1:
            return True if s[i] == p[j] or p[j] == "." else False

        if j == len(p) - 1 and i != len(s) - 1:
            return False

        # if j+1 is *
        if j < len(p) - 1 and p[j + 1] == "*":
            if search(i, j + 2):  # Skip the '*' pattern
                return True
            if i < len(s) and (s[i] == p[j] or p[j] == "."):
                ans = False
                while i <= len(s) and (
                    p[j] == "." or i < len(s) and j < len(p) and s[i] == p[j]
                ):
                    ans = ans or search(i, j + 2)
                    i += 1
                if ans == True:
                    return ans

                return search(i, j + 2)

        # if j+1 is not *
        if (j < len(p) and i < len(s)) and (s[i] == p[j] or p[j] == "."):
            return search(i + 1, j + 1)

        return False

    return search(0, 0)


# print(isMatch("ab", ".*"))
# print(isMatch("ab", ".*c"))
# print(isMatch("aaa", "a*a"))
# print(isMatch("aaa", "a*c"))
# print(isMatch("a", "b*c*a"))
# print(isMatch("a", "a*a"))
print(isMatch("aab", "a*b"))

# i is at end:
# j is at end: conditional return
# j is not at end: False
# j is at end:
# i is at end: conditional return
# i is not at end: False
# if i exceeds bound:
# if j also exceeds bound: return True
# if j does not exceeds bound: return True, maybe false
# if j exceeds bound:
# if i does not exceeds bound:return False
# if i exceeds bound: return True
