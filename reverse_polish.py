from collections import deque
import math


def is_valid_integer(s):
    if s[0] == "-":
        return s[1:].isdigit()
    return s.isdigit()


def reverse_polish(tokens):
    stack = deque()
    operations = {"+", "-", "/", "*"}
    for token in tokens:
        if is_valid_integer(token):
            stack.append(int(token))
        if token in operations:
            first_operand = stack.pop()
            second_operand = stack.pop()
            if token == "+":
                result = second_operand + first_operand
            if token == "-":
                result = second_operand - first_operand
            if token == "/":
                result = second_operand // first_operand
            if token == "*":
                result = second_operand * first_operand
            stack.append(result)

    return stack[0]


print(reverse_polish(["4", "13", "5", "/", "+"]))
