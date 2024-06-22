def minWindow(s, t):
    res = float("inf")
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
    sum = 0
    final_string = ""
    while r < len(s):
        if s[r] in target:
            if duplicate_target[s[r]] > 0:
                sum += 1
            duplicate_target[s[r]] -= 1
        if sum < target_sum:
            r += 1
        elif sum == target_sum:
            while sum == target_sum:
                if r - l + 1 < res:
                    res = r - l + 1
                    final_string = s[l : r + 1]
                if s[l] in target:
                    duplicate_target[s[l]] += 1
                    if duplicate_target[s[l]] > 0:
                        sum -= 1
                l += 1
            r += 1
    return final_string


print(minWindow("codebanc", "abc"))
