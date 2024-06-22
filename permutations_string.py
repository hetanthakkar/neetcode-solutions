def permutation_string(s1, s2):

    window = {}

    upcoming = []
    for char in s1:
        if char in window:
            window[char] += 1
        else:
            window[char] = 1
    duplicate_window = window.copy()
    sum = len(window)
    leftPointer = rightPointer = 0
    while rightPointer < len(s2):
        if (
            s2[rightPointer] in duplicate_window
            and duplicate_window[s2[rightPointer]] > 0
        ):
            duplicate_window[s2[rightPointer]] -= 1
            sum -= 1
            rightPointer += 1

        else:
            if s2[rightPointer] in duplicate_window:
                duplicate_window[s2[leftPointer]] += 1
                sum += 1
                leftPointer += 1
            else:
                rightPointer += 1
                leftPointer = rightPointer
                duplicate_window = window.copy()

    return sum == 0


# print(permutation_string("adc", "dcda"))
print(permutation_string("hello", "ollelh"))
