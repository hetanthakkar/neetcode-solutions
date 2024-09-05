def maxHeightOfTriangle2(red, blue):
    red_count = red
    blue_count = blue
    intital = 0
    level = 0
    while red_count != 0 and blue_count != 0:
        level += 1
        if intital == 0:
            red_count -= level
        else:
            blue_count -= level
        if blue_count < 0 or red_count < 0:
            level -= 1
            break
        if blue_count == 0 and red_count == 0:
            break
        intital = 1 if intital == 0 else 0
    return level


def maxHeightOfTriangle1(red, blue):
    red_count = red
    blue_count = blue
    intital = 1
    level = 0
    while red_count != 0 and blue_count != 0:
        level += 1
        if intital == 0:
            red_count -= level
        else:
            blue_count -= level
        if blue_count < 0 or red_count < 0:
            level -= 1
            break
        if blue_count == 0 and red_count == 0:
            break
        intital = 1 if intital == 0 else 0
    return level


def main(red, blue):
    print(maxHeightOfTriangle1(red, blue))
    print(maxHeightOfTriangle2(red, blue))
    return max(maxHeightOfTriangle1(red, blue), maxHeightOfTriangle2(red, blue))


print(main(1, 1))
