# def encode( arr):
#     concs=""
#     for s in arr:
#         concs+=s

#     count=0
#     for ar in arr:
#         count=count+len(ar)    
#     concs += str(count)
#     new=""
#     for s in arr:
#         s+=concs
#         new+=s
#     # print(concs)
#     l=decode(new)    
#     return l


# def decode(str):
    
#     arr=[]
#     for ind in range(0,len(str)):
#         if str[ind].isdigit():
#             to=ind-int(str[ind])-1
#             strin=""
#             while(to>=0):
#                 if str[to].isdigit():
#                     break
#                 strin+=str[to]
#                 to=to-1
#             print(strin[::-1],"string")
#             arr.append(strin[::-1])

#     return arr




# print(encode(["a","b","c","de"]))



def encode( arr):
    concs=""
    for s in arr:
        concs+=s
    count=0    
    for t in concs:
        count=count+ord(t)

    print(count)
    # for ar in arr:
    #     count=count+len(ar)    
    # concs += str(count)
    # new=""
    # for s in arr:
    #     s+=concs
    #     new+=s
    # # print(concs)
    # l=decode(new)    
    # return l


def decode(str):
    
    arr=[]
    for ind in range(0,len(str)):
        if str[ind].isdigit():
            to=ind-int(str[ind])-1
            strin=""
            while(to>=0):
                if str[to].isdigit():
                    break
                strin+=str[to]
                to=to-1
            print(strin[::-1],"string")
            arr.append(strin[::-1])

    return arr




print(encode(["a","b","c","de"]))