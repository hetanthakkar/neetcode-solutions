class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        if len(self.stack) == 0:
            self.stack.append(val)
            self.min_stack.append(val)
        else:
            top = self.min_stack[-1]
            self.stack.append(val)
            if top <= val:
                element = self.min_stack.pop()
                self.min_stack.append(val)
                self.min_stack.append(element)
            else:
                self.min_stack.append(val)

    def pop(self):
        min = self.min_stack[-1]
        top = self.stack[-1]
        if min < top:
            minimum = self.min_stack.pop()
            self.min_stack.pop()
            self.min_stack.append(minimum)
        if top == min:
            self.min_stack.pop()
        self.stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return min(self.min_stack[-1], self.stack[-1])


minStack = MinStack()
minStack.push(2)
minStack.push(0)
minStack.push(3)
minStack.push(0)
print(minStack.getMin())
minStack.pop()
print(minStack.getMin())
minStack.pop()
print(minStack.getMin())
minStack.pop()
print(minStack.getMin())

# print(minStack.top())
# print(minStack.getMin())

# mn = MinStack()
