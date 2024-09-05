def longestCommonSubsequence(text1, text2):
    def search(i, j):
        if i == len(text1) or j == len(text2):
            return 0
        if text1[i] == text2[j]:
            count1 = 1 + search(i + 1, j + 1)
        else:
            count1 = 0
        count2 = search(i + 1, j)
        count3 = search(i, j + 1)
        return max(count1, count2, count3)

    return search(0, 0)


text1 = "a"
text2 = "aa"
print(longestCommonSubsequence(text1, text2))
print("asdkj")
