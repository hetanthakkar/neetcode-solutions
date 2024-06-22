dp={}
def longest_palindromic_substring(s):
    
    if (len(s)==1):
        dp[s]=s
        return s
    
    if (len(s)==0):
        return ""
    
    if s in dp:
        return dp[s]
    
    center = len(s) // 2
    
    left, right = center - 1, center + len(s) % 2

    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1

    new= s[left + 1:right]
    if s[:-1] in dp:
            str2=dp[s[:-1]]
    else:
        str2=longest_palindromic_substring(s[:-1])
    if s[1:] in dp:
        str1=dp[s[1:]]
    else:
        str1=longest_palindromic_substring(s[1:])
    longest_str = max(str1, str2, new, key=len)  
    dp[s] = longest_str
    print(dp)
    return(longest_str)


# def longest_palindromic_substring_bottom_up(s):
#     n = len(s)

#     if n <= 1:
#         return s

#     dp = [[False] * n for _ in range(n)]

#     start, max_len = 0, 1

#     # All substrings of length 1 are palindromes
#     for i in range(n):
#         dp[i][i] = True

#     # Check substrings of length 2
#     for i in range(n - 1):
#         if s[i] == s[i + 1]:
#             dp[i][i + 1] = True
#             start = i
#             max_len = 2

#     # Check substrings of length 3 or more
#     for length in range(3, n + 1):
#         for i in range(n - length + 1):
#             j = i + length - 1

#             # Check if the current substring is a palindrome
#             if dp[i + 1][j - 1] and s[i] == s[j]:
#                 dp[i][j] = True

#                 # Update start and max_len if current palindrome is longer
#                 if length > max_len:
#                     start = i
#                     max_len = length

#     return s[start:start + max_len]

# # Example usage
# s = "babad"
# result = longest_palindromic_substring_bottom_up(s)
# print(result)
print(longest_palindromic_substring("aaa"))
print(len(set(dp.keys())))





