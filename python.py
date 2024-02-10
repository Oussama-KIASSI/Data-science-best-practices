### Use the Right Comparator
## Example of using .startswith() and .endswith() instead of string slicing
text = "Hello, world!"
if text.startswith("Hello"):
    print("Text starts with 'Hello'")
if text.endswith("!"):
    print("Text ends with '!'")

## Example of using isinstance() for type checking
number = 10
if isinstance(number, int):
    print("Number is an integer")

## Example of using implicit false if possible
empty_list = []
if not empty_list:
    print("List is empty")

## Example of using is or is not to compare singletons like None
value = None
if value is None:
    print("Value is None")

## Example of using is not operator over not ... is
value = 0
if value is not None:
    print("Value is not None")


### Use Conditional Expressions for simple cases
a = 10
b = 20

max_number = a if a > b else b
print("The maximum number is:", max_number)


### Annotate Python Code with Type Hints
def greet(name: str) -> str:
    return f"Hello, {name}!"

result: str = greet("Alice")
print(result)


### Avoid Using + and += Operators for String Accumulation
# Bad practice
result = ""
for i in range(10):
    result += str(i)
print(result)  # Output: "0123456789"

# Better practice
result_list = []
for i in range(10):
    result_list.append(str(i))
result = "".join(result_list)
print(result)  # Output: "0123456789"


### Avoid Mutable Global State
# Bad practice
global_list = []

def add_to_list(item):
    global global_list
    global_list.append(item)

add_to_list(1)
print(global_list)  # Output: [1]

add_to_list(2)
print(global_list)  # Output: [1, 2]

# Better practice
def add_to_list(input_list, item):
    return input_list + [item]

my_list = []
my_list = add_to_list(my_list, 1)
print(my_list)  # Output: [1]

my_list = add_to_list(my_list, 2)
print(my_list)  # Output: [1, 2]


### Use Context Managers to securely manage external resources
# Bad practice
file = open("example.txt", "r")
content = file.read()
print(content)
file.close()  # Don't forget to close the file

# Better practice
with open("example.txt", "r") as file:
    content = file.read()
    print(content)  # File is automatically closed after exiting the 'with' block


### Use Keyword Arguments Whenever Possible
# Bad practice
def greet(name, greeting):
    return f"{greeting}, {name}!"

print(greet("Alice", "Hello"))  # Output: "Hello, Alice!"

# Better practice
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Alice"))  # Output: "Hello, Alice!"


### Use Immutable Default Arguments
# Bad practice
def add_item(item, my_list=[]):
    my_list.append(item)
    return my_list

print(add_item(1))  # Output: [1]
print(add_item(2))  # Output: [1, 2]

# Better practice
def add_item(item, my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(item)
    return my_list

print(add_item(1))  # Output: [1]
print(add_item(2))  # Output: [2]


### Use Absolute Import for Single Function Imports
from utils.math_operations import add


### Use Relative Import for Long Absolute Paths
# Bad practice
from utilities.tools.helper_functions import extract_data

# Better practice
from .helper_functions import extract_data

### Use Blank Lines for Separation
## Surround top-level functions and class definitions with two blank lines.
def function_one():
    pass


class MyClass:
    pass


def function_two():
    pass


## Surround method definitions inside classes by single blank lines.
class MyClass:
    def method_one(self):
        pass

    def method_two(self):
        pass


## Surround groups of related functions by single blank lines.
def group_one_function_one():
    pass

def group_one_function_two():
    pass


def group_two_function_one():
    pass


## Surround groups of similar category libraries by single blank lines.
# Group of math-related functions
def math_function_one():
    pass

def math_function_two():
    pass


# Group of string-related functions
def string_function_one():
    pass

def string_function_two():
    pass


## Surround logical sections inside functions by single blank lines.
def my_function():
    # Logical section one
    x = 1
    y = 2

    # Logical section two
    z = x + y

    return z


### Avoid Extraneous Whitespace:
## Inside parentheses, brackets, or braces.
my_list = [1, 2, 3,]
my_dict = {'a': 1, 'b': 2}

## Between a trailing comma and a following close parenthesis.
my_tuple = (1, 2, 3,)

## Immediately before a comma, semicolon, or colon.
x = 10 ; y = 20

## Immediately before the open parenthesis that starts the argument list of a function call.
result = my_function(10, 20)

## Immediately before the open parenthesis that starts an indexing or slicing.
my_string = "hello"[0]

## Around an assignment operator but not a keyword argument or a default value for an unannotated function parameter.
a = 10
b = 20

## At the end of statements.
print("Hello World")


## Use Trailing Comma for Lists and Imports
my_list = [
    1,
    2,
    3,  # Trailing comma
]

from math import (
    pow,
    ceil,
)  # Trailing comma

## Separate Blocks with Comments
# Block 1
x = 10
y = 20

# Block 2
z = x + y
print(z)

## Separate paragraphs inside a block comment by a line containing a single #
"""
This is a block comment.

Paragraph 1.

#
Paragraph 2.
"""

## Separate inline comments by at least two spaces from the statement
result = my_function(10, 20)  # Inline comment separated by two spaces


### Use Args, Attributes, Returns, and Raises Sections
def calculate_area(length: float, width: float) -> float:
    """
    Calculate the area of a rectangle.

    Args:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.

    Returns:
        float: The calculated area of the rectangle.

    Raises:
        ValueError: If either length or width is negative.
    """
    if length < 0 or width < 0:
        raise ValueError("Length and width must be non-negative.")
    return length * width
