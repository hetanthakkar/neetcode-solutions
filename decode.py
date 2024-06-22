# import string
# alphabet=string.ascii_lowercase
# def decode1(n,s,max):
#     if (s[n-1]=="0" and len(s)==2) or s=="0":
#         return 0
#     if n==0:
#         max=max+1
#         return 1
#     a=s[n-1]
#     b=s[n]
#     # d=alphabet.find("25")
#     d=decode1(n-1,s,max)
#     if s[n-1]=="0":
#         return d-1
#     c=int(a+b)
#     # if c<=26 and len(s)>2:

#     if c<=26 and len(s)>3:
#         return d+len(s[0:n])-2
        
#     if c<=26:
#         return d+1

    
    
#     return decode1(n-1,s,max)
def numDecodings( s):
        if not s or s[0] == '0':
            return 0

        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n + 1):
            one_digit = int(s[i - 1])
            two_digits = int(s[i - 2:i])

            if one_digit != 0:
                dp[i] += dp[i - 1]

            if 10 <= two_digits <= 26:
                dp[i] += dp[i - 2]

        return dp[n]

print(numDecodings("11223"))


# 120
