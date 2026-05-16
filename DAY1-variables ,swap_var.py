#  Problem: a=5 and b=10 ko swap karo.
# Method 1: 3rd Variable – Safe for all languages
a, b = 5, 10
temp = a
a = b
b = temp
print(a, b)  # 10 5

# Method 2: Pythonic – 1 Line, sbse  best method
a, b = 5, 10
a, b = b, a  # Tuple unpacking
print(a, b)  # 10 5

# Method 3: Arithmetic – No extra variable
a, b = 5, 10
a = a + b  # a=15
b = a - b  # b=15-10=5
a = a - b  # a=15-5=10
print(a, b)  # 10 5
