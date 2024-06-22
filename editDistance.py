def callEditDistance(i,j,word1, word2,dp):
    if i>=len(word1) and j>=len(word2):
        return 0
    if i>=len(word1) or j>=len(word2):
        return abs(abs(len(word1)-i)-abs(len(word2)-j))

    if i>=len(word1) or j>=len(word2) and word1[i]==word2[j]:
        return 0

    if dp[i][j]!=-1:
        return dp[i][j]
        
    
    if word1[i]==word2[j]:
        return callEditDistance(i+1,j+1,word1,word2,dp)
    else:    

        replace=callEditDistance(i+1,j+1,word1,word2,dp)+1
        delete=callEditDistance(i+1,j,word1,word2,dp)+1
        add=callEditDistance(i,j+1,word1,word2,dp)+1
        dp[i][j]=min(replace,add,delete)
        return dp[i][j]

def editDistance(word1,word2):
    dp = [[-1 for _ in range(len(word2)+ 1)] for _ in range(len(word1) + 1)]
    return callEditDistance(0,0,word1,word2,dp)  

print(editDistance("horse","ros"))