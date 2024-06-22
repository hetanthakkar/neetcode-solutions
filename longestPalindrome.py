# def palindrome1(str,dp):
#     i=0
#     if str=="":
#         return ""
#     if len(str)==1:
#         return str
#     current_char=str[i]
#     reversed_string=str[::-1]
#     if len(str)==2:
#         if str[0]==str[1]:
#             return str
#         else:
#             return str[0]
#     if dp[str]!=-1:
#         return dp[str]
#     str1=""
#     found=None
#     for j in range(0,len(reversed_string)): 
#         # print(str[j])
#         if reversed_string[j] == current_char:
#             found=len(str)-j-1
#             break
#     if found:
#         print(str[i+1:found],i,str[i+1:])
#         temp1=str[i+1:found]
#         temp2=palindrome1(str[i+1:found])
#         if len(temp1)==len(temp2):
#             str1=str[i]+temp2+str[i]
#         else:
#             str1=str[i]
#     else:
#         str1=""    
#     k= str[i+1:]
#     str2=palindrome1(str[i+1:])
#     if len(str1)>len(str2):
#         dp[str]:str1
#         return str1
#     else:
#         dp[str]=str2
#         return str2

def palindrome2(str,dp):
    i=0
    if str=="":
        return ""
    
    if len(str)==1:
        return str
    current_char=str[i]
    reversed_string=str[::-1]
    
    if len(str)==2:
        if str[0]==str[1]:
            return str
        else:
            return str[0]
    
    if str in dp:
        return dp[str]
    
    str1=""
    found=None
    
    for j in range(0,len(reversed_string)): 
        if reversed_string[j] == current_char:
            found=len(str)-j-1
            break
    if found:
        print(str[i+1:found],i,str[i+1:])
        temp2=palindrome2(str[i+1:found],dp)
        search_string=str[i]+temp2+str[i]
        if search_string not in str:
            str1=str[i]
        else:
            str1=str[i]+temp2+str[i]


    else:
        str1=""    
        str2=palindrome2(str[i+1:],dp)
        str3=palindrome2(str[1:],dp)
        str4=palindrome2(str[:-1],dp)
    if max(len(str1),len(str2),len(str3),len(str4))==len(str1):
        dp[str]=str1
        return str1
    
    if max(len(str1),len(str2),len(str3),len(str4))==len(str2):
        dp[str]=str2
        return str2
    

    if max(len(str1),len(str2),len(str3),len(str4))==len(str3):
        dp[str]=str3
        return str3
    
    if max(len(str1),len(str2),len(str3),len(str4))==len(str4):
        dp[str]=str4
        return str4




def longest(s):
    dp={}
    return palindrome2(s,dp)
print(longest("aaaabbaa"))    