def isPalindrome(s, i, j):
    if s[i : j + 1] == s[i : j + 1][::-1]:
        return True
    else:
        return False


def search(i, j, solutions, s):
    if j == len(s):
        return
    if isPalindrome(s, i, j):
        solutions.append(s[i : j + 1])
    search(i, j + 1, solutions, s)


def main(s):
    solutions = []
    for i in range(0, len(s)):
        search(i, i, solutions, s)
    return len(solutions)


print(main("aba"))
