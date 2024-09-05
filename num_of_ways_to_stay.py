def numWays(steps, arrLen):

    def search(steps_left, position):
        count = 0
        if steps_left == 0:
            if position == 0:
                count += 1
                return count
            else:
                return 0
        if position < 0 or position >= arrLen:
            return 0
        # stay
        option1 = search(steps_left - 1, position)
        # right
        option2 = search(steps_left - 1, position + 1)
        # left
        option3 = search(steps_left - 1, position - 1)

        return option1 + option2 + option3

    return search(steps, 0) % (10**9 + 7)


print(numWays(4, 2))
