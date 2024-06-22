def partitionLabels(s):
    dictionary = {}
    for index, char in enumerate(s):
        if char not in dictionary:
            dictionary[char] = [index]
    for index, char in enumerate(reversed(s)):
        if len(dictionary[char]) == 1:
            dictionary[char].append(len(s) - index - 1)
    lowerRange = upperRange = -1
    groups = {}
    for key, values in dictionary.items():
        if upperRange == -1 or lowerRange == -1:
            if lowerRange == -1:
                lowerRange = values[0]
            if upperRange == -1:
                if values[1]:
                    upperRange = values[1]
                else:
                    upperRange = values[0]
            groups[lowerRange] = upperRange
        else:
            if not (values[0] > upperRange or values[1] < lowerRange):
                upperRange = max(values[1], upperRange)
                lowerRange = min(values[1], lowerRange)
                groups[lowerRange] = upperRange
            else:
                upperRange = values[1]
                lowerRange = values[0]
                groups[lowerRange] = upperRange
    print(groups)
    answer = []
    for key, values in groups.items():
        answer.append(values - key + 1)
    return answer


print(partitionLabels("caedbdedda"))
