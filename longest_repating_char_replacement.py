def charReplacement(s, k):
    l = r = 0
    temp_k = k
    max_length = 0
    main_element = s[0]
    while r < len(s):

        if temp_k > 0 or s[r] == main_element:
            if s[r] != main_element:
                temp_k -= 1
            max_length = max(max_length, r - l + 1)
            r += 1
            continue

        if temp_k == 0 and s[r] != main_element:
            max_length = max(max_length, r - l)
            main_element = s[r]
            while temp_k <= 0:
                l += 1
                if l < len(s) and s[l] == main_element:
                    temp_k += 1
            if r < len(s):
                main_element = s[r - 1]
            continue

    return max_length


print(charReplacement("AABA", 0))
