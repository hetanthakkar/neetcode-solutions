
def clash(stones,i,j):
        if len(stones)==1:
            return stones[0]
        x=stones[0]
        y=stones[1]
        if x>y:
            x, y = y,x
        clash_stone_array=stones.copy()
        clash_stone_array.remove(x)
        clash_stone_array.remove(y)
        clash_stone_array.append(y-x)
        weight1=clash(clash_stone_array)
        unclash_stone_array=stones.copy()
        unclash_stone_array.remove(x)
        weight2 = x - clash(unclash_stone_array)
        return min(weight1,weight2)

print(clash([2,7,4,1,8,1]))


