def palindrome2(str,dp):
    str1=""
    if str=="":
        return ""
    if len(str)==1:
        return str
    if len(str)==2:
        if str[0]==str[1]:
            return str
        else:
            return str[0]
    if str in dp:
        return dp[str]
    found=None
    current_char=str[0]
    new=str[1:]
    reversed_string=new[::-1]
    for j in range(0,len(reversed_string)): 
        if reversed_string[j] == current_char:
            found=len(str)-j-1
            break
    if found:
        temp2=palindrome2(str[1:found],dp)
        search_string=str[0]+temp2+str[0]
        if search_string not in str:
            str1=str[0]
        else:
            str1=str[0]+temp2+str[0]        

    str2=palindrome2(str[1:],dp)
    str3=palindrome2(str[1:-1],dp)
    str4=palindrome2(str[:-1],dp)
    longest_str = max(str1, str2, str3, str4, key=len)
    dp[str] = longest_str
    return longest_str

   

def longest(s):
    dp={}
    return palindrome2(s,dp)
print(longest("abbcccbbbcaaccbababcbcabca"))    