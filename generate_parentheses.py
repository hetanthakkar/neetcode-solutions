from collections import deque


def insert_char_at_index(s, index, char):
    return s[:index] + char + s[index:]


def generateParenthesis1(brackets):
    brackets_stack = deque()
    result_stack = deque()
    for _ in range(brackets - 1):
        brackets_stack.append("()")
    if len(result_stack) == 0:
        result_stack.append("()")

    while len(brackets_stack) != 0:
        temp = []
        while len(result_stack) != 0:
            temp.append(result_stack[-1])
            result_stack.pop()
        top = brackets_stack[-1]
        for k in temp:
            for i in range(0, len(k)):
                res = insert_char_at_index(k, i, top)
                result_stack.append(res)
        if len(brackets_stack) != 0:
            brackets_stack.pop()
    ab = set()
    for i in result_stack:
        if len(i) == (brackets) * 2:
            ab.add(i)

    return list(ab)


print(generateParenthesis1(4))
