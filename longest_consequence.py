def longestConsecutive(nums):
    if not nums:
        return 0
    max_len = 1
    seen = set()
    duplicate_set = set(nums)
    for i in nums:
        if i not in seen:
            curr_len = 1
            seen.add(i)
            low = i - 1
            high = i + 1
            found = low in duplicate_set or high in duplicate_set
            while found:
                if low in duplicate_set:
                    seen.add(low)
                    curr_len += 1
                    low -= 1
                if high in duplicate_set:
                    seen.add(high)
                    curr_len += 1
                    high += 1
                max_len = max(max_len, curr_len)
                found = low in duplicate_set or high in duplicate_set
    return max_len


print(longestConsecutive([3, 2, 4, 5]))
