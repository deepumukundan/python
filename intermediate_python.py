# 1. List Comprehensions (various patterns)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Basic list comprehension
squares = [x**2 for x in numbers]
print(f"Squares: {squares}")

# With condition
evens = [x for x in numbers if x % 2 == 0]
print(f"Even numbers: {evens}")

# Nested list comprehension
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [item for row in matrix for item in row]
print(f"Flattened: {flattened}")

# Dictionary comprehension
word_lengths = {word: len(word) for word in ['python', 'java', 'javascript']}
print(f"Word lengths: {word_lengths}")

# Set comprehension
unique_remainders = {x % 3 for x in numbers}
print(f"Unique remainders: {unique_remainders}")

# 2. Multiple Assignment and Unpacking
# Basic multiple assignment
a, b, c = 1, 2, 3
print(f"a={a}, b={b}, c={c}")

# Swapping variables (Pythonic way)
x, y = 10, 20
x, y = y, x
print(f"After swap: x={x}, y={y}")

# Unpacking lists/tuples
data = [1, 2, 3, 4, 5]
first, *middle, last = data
print(f"First: {first}, Middle: {middle}, Last: {last}")

# Unpacking in function calls
def greet(first, last, age):
    return f"Hello {first} {last}, age {age}"

person = ("John", "Doe", 30)
message = greet(*person)
print(message)

# Unpacking dictionaries
def create_user(name, email, age):
    return f"User: {name}, {email}, {age}"

user_data = {"name": "Alice", "email": "alice@email.com", "age": 25}
result = create_user(**user_data)
print(result)

# 3. Enumerate and Zip
fruits = ['apple', 'banana', 'cherry']

# Enumerate for index and value
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")

# Zip for combining iterables
colors = ['red', 'yellow', 'dark red']
for fruit, color in zip(fruits, colors):
    print(f"{fruit} is {color}")

# Zip with different lengths (stops at shortest)
numbers = [1, 2, 3, 4, 5]
letters = ['a', 'b', 'c']
combined = list(zip(numbers, letters))
print(f"Combined: {combined}")

# 4. Lambda Functions and Built-in Functions
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Map with lambda
squared = list(map(lambda x: x**2, numbers))
print(f"Squared with map: {squared}")

# Filter with lambda
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Evens with filter: {evens}")

# Sorted with custom key
words = ['python', 'java', 'c', 'javascript', 'go']
by_length = sorted(words, key=lambda x: len(x))
print(f"Sorted by length: {by_length}")

# Max/min with key
longest_word = max(words, key=len)
print(f"Longest word: {longest_word}")

# 5. String Formatting Methods
name = "Alice"
age = 30
score = 95.67

# f-strings (Python 3.6+) - most preferred
print(f"Hello {name}, you are {age} years old")
print(f"Score: {score:.1f}")  # 1 decimal place

# .format() method
print("Hello {}, you are {} years old".format(name, age))
print("Score: {:.2f}".format(score))  # 2 decimal places

# Named placeholders
template = "Name: {name}, Age: {age}, Score: {score:.1f}"
print(template.format(name=name, age=age, score=score))

# 6. Useful Built-in Functions
numbers = [3, 1, 4, 1, 5, 9, 2, 6]

# any() and all()
print(f"Any even numbers? {any(x % 2 == 0 for x in numbers)}")
print(f"All positive? {all(x > 0 for x in numbers)}")

# sum() with generator expression
total_squares = sum(x**2 for x in numbers)
print(f"Sum of squares: {total_squares}")

# range() tricks
print(f"Countdown: {list(range(10, 0, -1))}")
print(f"Even numbers: {list(range(0, 11, 2))}")

# 7. Default Dictionary and Counter
from collections import defaultdict, Counter

# defaultdict avoids KeyError
word_count = defaultdict(int)
text = "hello world hello python"
for word in text.split():
    word_count[word] += 1
print(f"Word count: {dict(word_count)}")

# Counter for counting
letters = Counter("hello world")
print(f"Letter frequency: {letters}")
print(f"Most common: {letters.most_common(3)}")

# 8. Ternary Operator
x = 10
# Instead of if-else block
result = "positive" if x > 0 else "negative or zero"
print(f"{x} is {result}")

# In list comprehensions
numbers = [-2, -1, 0, 1, 2]
signs = ["positive" if x > 0 else "negative" if x < 0 else "zero" for x in numbers]
print(f"Signs: {signs}")

# 9. Slicing Tricks
data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(f"Every 2nd element: {data[::2]}")
print(f"Reverse: {data[::-1]}")
print(f"Last 3: {data[-3:]}")
print(f"All but first and last: {data[1:-1]}")

# Slice assignment
data[2:5] = [20, 30, 40]
print(f"After slice assignment: {data}")

# 10. Generator Expressions (memory efficient)
# List comprehension vs generator expression
squares_list = [x**2 for x in range(1000)]  # Creates list in memory
squares_gen = (x**2 for x in range(1000))   # Creates generator

# Generator for large datasets
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Get first 10 fibonacci numbers
fib_gen = fibonacci()
first_10_fib = [next(fib_gen) for _ in range(10)]
print(f"First 10 Fibonacci: {first_10_fib}")

# Generator expression with sum
sum_of_squares = sum(x**2 for x in range(100))
print(f"Sum of squares 0-99: {sum_of_squares}")

# dict merge
a = {'a': 1, 'b': 2}
b = {'c': 3, 'd': 4}
print (a|b)

print("\n--- Quick Examples Summary ---")
print("List comp: [x*2 for x in range(5)]")
print("Dict comp: {x: x**2 for x in range(3)}")
print("Unpack: a, *rest, b = [1, 2, 3, 4, 5]")
print("f-string: f'{name} is {age} years old'")
print("Lambda: max(words, key=lambda x: len(x))")
print("Ternary: 'big' if x > 10 else 'small'")
print("Generator: (x**2 for x in range(100))")