def isPalindrome(s):
    result = ""
    for char in s:
        if char.isdigit() or char.isalpha():
            if char.isupper():
                char = char.lower()
            result += char
    leftPointer = 0
    rightPointer = len(result) - 1
    isPalindrome = True
    while leftPointer < rightPointer:
        if result[leftPointer] != result[rightPointer]:
            return False
        else:
            leftPointer += 1
            rightPointer -= 1
    return isPalindrome


print(len(isPalindrome(":")))
