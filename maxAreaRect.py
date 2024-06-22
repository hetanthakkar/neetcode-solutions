def maxAreaRect(heights):
    temp={"area":0,"width":0,"minHeight":0,"index":-1}
    for t  in range(0,len(heights)):
        height=heights[t]
        a=(int(temp["width"])+1)
        b=min(temp["minHeight"],height)
        if height>(a*b):
            temp={"area":height,"width":1,"minHeight":height,"index":t}
        if height==(a*b) and b!=height and abs(t-temp["index"])==1:
            temp={"area":height,"width":temp["width"]+1,"minHeight":temp["minHeight"],"index":t}
        if height<(a*b) and a*b>=temp["area"] and abs(t-temp["index"])==1:
            temp={"area":a*b,"width":temp["width"]+1,"minHeight":min(temp["minHeight"],height),"index":t}
    return temp["area"]

print(maxAreaRect([1,2,2]))