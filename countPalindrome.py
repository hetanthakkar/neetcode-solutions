count=[]
dp={}
def longest_palindromic_substring(s):
        
    if s in dp:
        # count.append({s:s})
        return dp[s]
    
    if (len(s)==1):
        dp[s]=s
        # t={}
        # t[s]=s
        # count.append({s:s})
        return s
    
    if (len(s)==0):
        return ""

    
    center = len(s) // 2
    
    left, right = center - 1, center + len(s) % 2

    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1

    new= s[left + 1:right]
    
    dp[new]=new
    if s[:-1] in dp:
            str2=dp[s[:-1]]
    else:
        str2=longest_palindromic_substring(s[:-1])
        # count.append({str2:str2})
    if s[1:] in dp:
        # count.append({s[1:]:s[1:]})
        str1=dp[s[1:]]
    else:
        str1=longest_palindromic_substring(s[1:])
        # count.append({str1:str1})
    a={new:new}
    b={str1:str1}
    c={str2:str2}
    if new !="":
        count.append({new:new})
    count.append({str1:str1}) 
    count.append({str2:str2})       
    
    longest_str = max(str1, str2, new, key=len)  
    
    dp[s] = longest_str
    print(dp)
    return(longest_str)



print(longest_palindromic_substring("abc"))
print(len(count),count)