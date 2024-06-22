def solution(S): 
    counter = 0
    V=int(S, 2)
    # V=bin(V)
    # print(type(V))
    # print(int(V))
    # V = int(S, 2)
  
    while (V > 0):

        if V&1==0:
            V = V >> 1
        
        else:
            V = V - 1
        
        counter+=1
    
    if V==1:
        return counter+1
    
    return counter

   
print(solution("111"))

