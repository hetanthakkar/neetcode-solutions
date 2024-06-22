def isInterleave(i,j,s1,s2,s3): 
    n1,n2,n3=len(s1),len(s2),len(s3)
    if n1+n2!=n3:
        return False
    if n1==1 or n2==1:
       return (s3==s1+s2 or s3==s2+s1)
    if n1>0 and n2>0 and (i>n1-1 or j>n2-1):
        return False
    
    if (s1[i]==s3[i] or s2[j]==s3[j]) :
        return True

    
    if(len(s3[0:i+j])!=0 and (s1[0:i]+s2[0:j]==s3[0:i+j] or s2[0:j]+s1[0:i]==s3[0:i+j])):
        return isInterleave(i+1,j+1,s1,s2,s3)
    else:    
        return isInterleave(i,j+1,s1,s2,s3) or isInterleave(i+1,j,s1,s2,s3)


print(isInterleave(0, 0, "ak", "cl", "aclk"))
