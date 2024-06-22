import math

def search1(i,j,matrix,target,type=False):
    # key = next(iter(dictionary))
    if len(matrix)==1:

        if next(iter(matrix[i]))==target:
            return i
        else:
             return i
    
    mid=math.floor((i+j)/2)
    
    if j-i==1:
        # ith=next(iter(matrix[i]))
        if target==next(iter(matrix[i])):
            return i
        if target==next(iter(matrix[j])):
            return j
        if target>next(iter(matrix[j])):
            return j
        if target<next(iter(matrix[j])):
            return i
        else:
            if type:
                return i
            else:
                return i
    if target>next(iter(matrix[mid])):
        return search1(mid,j,matrix,target,type)
    else:
        return search1(i,mid,matrix,target,type)
    
    
def binary_search(array,timestamp,type):
    return search1(0,len(array)-1,array,timestamp,type)
class TimeMap:
    values={}
    def __init__(self):
        self.values={}    

    def set(self, key, value, timestamp) -> None:
        if key not in self.values:
            self.values[key] = [(timestamp, value)]
        else:
            self.values[key].append((timestamp, value))
        # self.values[key].append((timestamp, value))
    def get(self, key, timestamp):
        if key not in self.values:
            return ""
        index = search1(0, len(self.values[key]) - 1, self.values[key], timestamp)
        if index == 0 and timestamp < self.values[key][0][0]:
            return ""
        return self.values[key][index][1]
tm=TimeMap()
tm.set("love","low",20)
tm.set("love","high",10)
tm.get("love",5)
tm.get("love",10)
tm.get("love",15)
tm.get("love",20)
tm.get("love",25)

a=[{1: 'bar'}, {4: 'bar1'}]
print(binary_search(a,10,False))
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

# {foo:[{1:"bar"}]}