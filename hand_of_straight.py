def isNStraightHand(hand, groupSize):
    hand.sort()
    dic = {}
    for card in hand:
        if card in dic:
            dic[card] += 1
        else:
            dic[card] = 1
    while dic:
        first = next(iter(dic.items()))[0]
        bucket = [first]
        dic[first] -= 1
        if dic[first] == 0:
            del dic[first]
        while len(bucket) < groupSize:
            if first + 1 in dic:
                bucket.append(first + 1)
                dic[first + 1] -= 1
                if dic[first + 1] == 0:
                    del dic[first + 1]
                first = first + 1
            else:
                return False
    return True


print(isNStraightHand([1, 2, 3, 6, 2, 3, 4, 7, 8, 9], 3))
