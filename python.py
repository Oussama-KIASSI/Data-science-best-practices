# Bad practice: Mutable global state
global_list = []

def add_to_list(item):
    global global_list
    global_list.append(item)

add_to_list(1)
print(global_list)  # Output: [1]

add_to_list(2)
print(global_list)  # Output: [1, 2]


# Better practice: Avoid mutable global state using function parameters and return values
def add_to_list(input_list, item):
    return input_list + [item]

my_list = []
my_list = add_to_list(my_list, 1)
print(my_list)  # Output: [1]

my_list = add_to_list(my_list, 2)
print(my_list)  # Output: [1, 2]
