def maxArea(height):
        new = []
        for i in range(len(height)):
            new.append({"index": i, "height": height[i]})
        
        sorted_array = sorted(new, key=lambda x: x['height'])
        arr=[]
        for i in sorted_array:
              h=i["height"]
              t=max(abs(0-i["index"]),abs((len(height)-1)-i["index"]))
              if t==abs(0-i["index"]):
                    h=min(i["height"],height[0])
              else:
                    h=min(i["height"],height[len(height)-1])
                    
              arr.append({"height":h*t,"index":i["index"]})
        arr = sorted(arr, key=lambda x: x['height'],reverse=True)
        x=arr[0]["index"]
        print(x)
        arr1=[]
        for i in new:
            if arr[0]["index"]==i["index"]:
                    continue
            width=abs(i["index"]-x)
            # print(width)
            height1=min(height[x],i["height"])
            # print(height)
            arr1.append({"area":width*height1,"index":i["index"]})
        arr1 = sorted(arr1, key=lambda x: x['area'],reverse=True)
        print(arr1[0]["area"])
        
                      
        



    

maxArea([1,8,6,2,5,4,8,25,7])