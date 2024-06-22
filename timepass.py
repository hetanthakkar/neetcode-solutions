def isInterleave(i, j, s1, s2, s3, dp):
    if s1 + s2 == s3 or s2 + s1 == s3:
        return True
    n1 = len(s1)
    n2 = len(s2)
    n3 = len(s3)
    if i > n1 or j > n2:
        return False

    if dp[i][j] != -1:
        return dp[i][j]

    string = s1[0:i] + s2[0:j] + s1[i:n1] + s2[j:n2]

    if string == s3[0:i + j]:
        dp[i][j] = isInterleave(0, 0, s1[i:n1], s2[j:n2], s3[i + j:n3], dp)
    else:
        string1 = isInterleave(i + 1, j + 1, s1, s2, s3, dp)
        string2 = isInterleave(i + 1, j, s1, s2, s3, dp)
        string3 = isInterleave(i, j + 1, s1, s2, s3, dp)
        dp[i][j] = string1 or string2 or string3

    return dp[i][j]

def isInterleave1(s1, s2, s3):
    dp = [[-1 for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
    return isInterleave(0, 0, s1, s2, s3, dp)

print(isInterleave1("aabd", "abdc", "aabdabcd"))
