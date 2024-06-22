import re

s = "abc10okaf20"

# Use regular expression to separate alphabetic and numeric portions
result = re.findall('([a-zA-Z]+)(\d+)', s)

# Join the result to form the desired output
output = ' '.join([' '.join(pair) for pair in result])

print(output)