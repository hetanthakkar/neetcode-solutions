from collections import deque


def isValid(s):
    stars = []
    stack = deque()
    for index, char in enumerate(s):
        if char == "(":
            stack.append({char: index})
        elif char == ")":
            if stack and "(" in stack[-1]:
                stack.pop()
            else:
                if len(stars) > 0:
                    stars.pop(0)
                else:
                    stack.append({char: index})
        else:
            stars.append(index)

    if len(stack) > 0 and len(stars) > 0:
        while len(stack) != 0 and len(stars) > 0:
            top = stack[-1]
            key = next(iter(top))
            index = top[key]
            star_index = stars[-1]
            if key == ")":
                if index > star_index:
                    stack.pop()
            else:
                if index < star_index:
                    stack.pop()

            stars.pop(-1)

    return not bool(len(stack))


# print(isValid("(*))"))
# print(checkValidString1("())*((*)"))
# print(isValid("())))*)))*(*((*)))*)**(*(*))*))"))

# print(isValid("(*)"))  # True
# print(isValid("(*))"))  # True
# print(isValid("((*)"))  # True
# print(isValid("((*))"))  # True
# print(isValid("((*)*)"))  # True
# print(isValid("((*)**))"))  # True
# print(isValid("(()*"))  # True
# print(isValid("((((*)"))  # False
# print(isValid("*)*())"))
# print(
#     isValid(
#         ")(())(((((()())(()))))()(*()))()()()()((()(())())*((((())))*())()(()()))*((()(()(()))))(()())(*(*"
#     )
# )
print(isValid("*(*(*"))

# print(
#     isValid(
#         "()*()(()(*()(((())()()())*))()*()(*)(((*))(())(())((*()*(()(())()*(((*(**))((())*)(((()()))(())()))"
#     )
# )
# print(isValid("())*"))  # Output: False
