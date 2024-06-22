# a=[[]]
# c=2
# b=8
# suma=sum(a[len(a)-1])
# while(suma+1<=b):
#     t=[*a[len(a)-1]]
#     t.append(c)
#     a.append(t)
#     suma=sum(a[len(a)-1])

# print(a)
# ans=[]
# def combinationSum(n,nums,target):
#     if n==-1:
#         return [[]]
#     else:
#         prev=combinationSum(n-1,nums,target)
#         new=prev.copy()
#         for i in range(0,len(new)):
#             a=new[i].copy()
#             c=nums[n]
#             suma=sum(a)
#             while(suma+c<=target):
#                 t=a.copy()
#                 t.append(c)
#                 new.append(t)
#                 if sum(t)==target:
#                     ans.append(t)
#                 suma=sum(t)
#         a_filtered = [x for x in new if x not in prev]
#         prev.extend(a_filtered)

#         return prev

# print(combinationSum(2,[2,1],5))
