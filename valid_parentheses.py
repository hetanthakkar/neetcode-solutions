from collections import deque


def isValid(s):
    if len(s) == 1:
        return False
    else:
        stack = deque()
        brackets = {"[": "]", "(": ")", "{": "}"}

        for char in s:
            if char in brackets.values() and len(stack) == 0:
                return False
            if char in brackets:
                stack.append(char)
            if char in brackets.values() and len(stack) > 0:
                top = stack[-1]
                if char == brackets[top]:
                    stack.pop()
        return not bool(len(stack))


print(isValid("(])"))
