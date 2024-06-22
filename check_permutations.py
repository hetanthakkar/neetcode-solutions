def permutations(n, chars):
    if n == 0:
        return [[chars[0]]]
    else:
        prev = permutations(n - 1, chars)
        prev1 = []
        for temp in prev:
            for j in range(len(temp) + 1):
                new = temp.copy()
                new.insert(j, chars[n])
                prev1.append(new)
        return prev1


def permute(s: str):
    char_list = list(s)
    perm_list = permutations(len(char_list) - 1, char_list)
    return ["".join(p) for p in perm_list]


def chek_perm(s1, s2):
    temp = permute(s1)
    if s2 in temp:
        return True
    return False


# Example usage

print(chek_perm("eidbaooo", "ab"))
