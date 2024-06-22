class Solution:
    def permute(self, n, nums, is_valid):
        prev1 = []
        if n == 0:
            return [[nums[0]]] if (is_valid([nums[0]])) else []
        for temp in self.permute(n - 1, nums, is_valid):
            for j in range(len(temp) + 1):
                new_perm = temp[:j] + [nums[n]] + temp[j:]
                if is_valid(new_perm):
                    prev1.append(new_perm)
        return prev1


def is_valid(perm):
    if len(perm) != len(original):
        return True
    for i in range(len(perm)):
        if (
            perm[i] == original[i]
        ):  # Constraint: No number should be in its original index
            return False
    return True


# Example usage:
original = [1, 2, 3]
solution = Solution()
result = solution.permute(len(original) - 1, original, is_valid)
print(result)
