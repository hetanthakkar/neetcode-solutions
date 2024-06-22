def frequentArr(nums, k):
    res = []
    hash_map = {}
    for i in nums:
        if i not in hash_map:
            hash_map[i] = 1
        else:
            hash_map[i] += 1
    sorted_items = sorted(hash_map.items(), key=lambda x: x[1], reverse=True)
    for i in range(0, k):
        item = sorted_items[i][0]
        res.append(item)

    return res


print(frequentArr([1], 1))
