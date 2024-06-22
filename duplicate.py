strs = ["ac","d"]
def groupAnagrams(strs):
    count=1
    dic={}
    for str in strs:
        if str=="":
            dic[str]=count
            count=count+1
        for i in str:
            if i not in dic.keys():
                dic[i]=ord(i)
                count=count+1
    temp=[]
    print(dic,"ads")
    for str in strs:
        ct=0
        for i in str:
            print("heyt")
            ct=dic[i]+ct
        temp.append(ct)    
    print("asdf",temp)
    elements=[]
    ser=set(temp)
    for a in ser:
        indices = [strs[i] for i,val in enumerate(temp) if val==a]
        elements.append(indices)
    print(elements)
         
print (groupAnagrams(strs))