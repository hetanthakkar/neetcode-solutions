

def leastInterval(tasks,n):
    
    
    freq_array={}
    for i in tasks:
        if i in freq_array:
            freq_array[i]+=1
        else:
            freq_array[i]=1
    
    freq_array = dict(sorted(freq_array.items(), key=lambda x: x[1], reverse=True))

    count=0
    arr=["*" for _ in range(0,(n+1)*sum(freq_array.values()))]
    
    values_to_consider=freq_array.copy()
    for key,value in freq_array.items():
        
        new=count
        index=-1
        for i in range(0,len(arr)):
            if arr[i]=="*":
                index=i
                break
        new=index
        for j in range(count,len(arr)):
            # values_to_consider=freq_array.copy()
            if freq_array[key]!=0 and j<len(arr) and arr[j]=='*' and new<len(arr):
                arr[new]=key
                freq_array[key]=freq_array[key]-1 
                values_to_consider = {key: value for key, value in values_to_consider.items() if value != 0}   
                if len(values_to_consider.keys())-1>=n:
                    new=(new+1)+(len(values_to_consider.keys())-1)
                else:
                    if(arr[n+(new+1)]=="*"):
                        new=n+(new+1)
                    else:
                        ct=n+(new+1)
                        while arr[ct]!="*":
                            ct+=1
                        new =ct
            #  7
            # 2+4+   
                for key1,value in values_to_consider.items():
                    values_to_consider[key1]=value-1
                values_to_consider = {key: value for key, value in values_to_consider.items() if value != 0}
                
        count+=1       
    # 4 1+2+1
    while arr and arr[-1] == '*':
        arr.pop()
    print(arr)
    return len(arr)


# print(leastInterval(["G","H","A","G","G","F","G","J",],1))
# print(leastInterval(["A","B","C","D","E","A","B","C","D","E"],4))
# print(leastInterval(["A","A","A","B","B","B"],2))
# print(leastInterval(["A","B","C","D","E","A","B","C","D","E"],4))
print(leastInterval(["A","A","A","A","A","A","B","C","D","E","F","G"],1))



# ABCDEFGA*A*A*A*A
# A:6
# B:1
# C:1
# D:1
# E:1
# F:1
# G:1

# E:2
# G:2
# H:1
# C:1
# EGHCEG

# G:4
# h:1
# a:1
# f:1
# j:1
# G **** G*G*G



