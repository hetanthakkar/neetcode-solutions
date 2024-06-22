def isValid(s):
    stack = []
    star_indexes = []

    for i, char in enumerate(s):
        if char == "(":
            stack.append(i)
        elif char == "*":
            star_indexes.append(i)
        else:  # char == ')'
            if stack:
                stack.pop()
            elif star_indexes:
                star_indexes.pop()
            else:
                return False

    while stack and star_indexes:
        if stack[-1] > star_indexes[-1]:
            return False
        stack.pop()
        star_indexes.pop()

    return len(stack) == 0


a = "())))*)))*(*((*)))*)**(*(*))*))"

# print(isValid("((()))()(())(*()()())**(())()()()()((*()*))((*()*)"))
# print(isValid("*()((*)()*"))
# print(isValid("()((((()())))(*))((())*(((()))*)())*(((())))()(*(*"))
# print(isValid("((())(*))(*(()*))*(())(*(*"))
print(isValid("*(*(*"))
