def process(wordDict):
    dic=[]
    for word in wordDict:
        first=word[0]
        last=word[len(word)-1]
        dic.append([first,last,word])
    return dic

def wordbreak(left,right,s,wordDict):
    
    processedDict=process(wordDict)
    leftWord=None
    rightWord=None 

    if left-right>0:
        return True
    
    if left>=right:
        return False
    else:
        for word in processedDict:
            print(word)
            if s[left]==word[0]:
                leftWord=word[2]
                left+=1
                break
        for word in processedDict:
            if s[right]==word[1]:
                rightWord=word[2]
                right-=1
                break
        return wordbreak(left,right,s,wordDict)
    
    
    print(leftWord,rightWord)

print(wordbreak(0,2,"abc",["a","bc"]))