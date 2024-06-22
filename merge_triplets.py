def mergeTriplets(triplets, target):
    new = []
    for index, element in enumerate(triplets):
        if (
            triplets[index][0] <= target[0]
            and triplets[index][1] <= target[1]
            and triplets[index][2] <= target[2]
        ):
            new.append(element)
    if len(new) == 0:
        return False
    while len(new) != 1:
        new[0][0] = max(new[0][0], new[1][0])
        new[0][1] = max(new[0][1], new[1][1])
        new[0][2] = max(new[0][2], new[1][2])
        if new[0] != target:
            new.pop(1)
        else:
            return True
    if new[0] == target:
        return True
    else:
        return False


triplets = [
    [7, 15, 15],
    [11, 8, 3],
    [5, 3, 4],
    [12, 9, 9],
    [5, 12, 10],
    [7, 15, 10],
    [7, 6, 4],
    [3, 9, 8],
    [2, 13, 1],
    [14, 2, 3],
]
target = [14, 6, 4]
print(mergeTriplets(triplets, target))
