def total_fruits(fruits):
    dic = {}
    for fruit in fruits:
        if fruit in dic:
            dic[fruit] += 1
        else:
            dic[fruit] = 1
    sorted_dict = dict(sorted(dic.items(), key=lambda item: item[1], reverse=True))
    count = 0
    res = 0
    print(sorted_dict)
    for values in sorted_dict.values():
        if count < 2:
            res += values
        count += 1
    return res


print(total_fruits([3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]))
