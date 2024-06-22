def minimum_window_substring(s, t):
    res = []
    temp = []
    final = []
    target = {}
    for char in t:
        if char not in target:
            target[char] = 1
        else:
            target[char] += 1
    target_sum = 0
    for values in target.values():
        target_sum += values
    l = r = 0
    duplicate_target = target.copy()
    temp = []
    sum = 0

    while r < len(s):

        if s[r] in target:

            if duplicate_target[s[r]] > 0:
                sum += 1
            duplicate_target[s[r]] -= 1

        if sum < target_sum:
            if sum == 0 and s[l] not in target and s[r] not in target:
                l += 1
            if s[r] == s[l] and r != 0:
                l = r
                if s[l] in target:
                    duplicate_target[s[l]] += 1
            r += 1

        elif sum == target_sum:

            while sum == target_sum:
                if s[l] in target:
                    if duplicate_target[s[l]] < 0:
                        duplicate_target[s[l]] += 1
                    if duplicate_target[s[l]] >= 0:
                        sum -= 1
                if sum == target_sum:
                    break
                l += 1

            res.append(r - l + 1)
            r += 1

        elif sum > target_sum:

            while sum > target_sum or s[l] not in target:
                if s[l] in target:
                    sum -= 1
                l += 1
            res.append(r - l + 1)
            r += 1

        else:
            r += 1
    if len(res) == 0:
        return 0
    return min(res)


print(minimum_window_substring("codebanc", "abc"))
