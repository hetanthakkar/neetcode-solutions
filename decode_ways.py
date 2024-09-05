def solve(s):
    solutions = []
    count = 0
    memo = {}

    def search(current, last_digit):

        nonlocal solutions
        nonlocal count
        if (current, last_digit) in memo:
            return memo[(current, last_digit)]
        # if last digit becomes greater then 26 or last digit is 0 then return
        if last_digit and (int(last_digit) > 26 or int(last_digit) == 0):
            memo[(current, last_digit)] = 0
            return 0

        if current == len(s):
            memo[(current, last_digit)] = 1
            count += 1
            return 1

        # add seprately
        original = last_digit
        last_digit = s[current]
        result1 = search(current + 1, last_digit)
        last_digit = original

        # append to the last character
        original = last_digit
        last_digit = last_digit + s[current]
        result2 = search(current + 1, last_digit)
        last_digit = original
        memo[(current, last_digit)] = result1 + result2
        return result1 + result2

    return search(1, s[0])


# Example usage
print(solve("226"))
