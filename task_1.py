# Function to display variable types
def display_var_types():
    int_var = 10
    flt_var = 20.5
    str_var = "Hello, Main-Flow Technologies!"
    bool_var = True

    print(f"Integer: {int_var} (Type: {type(int_var)})")
    print(f"Float: {flt_var} (Type: {type(flt_var)})")
    print(f"String: {str_var} (Type: {type(str_var)})")
    print(f"Boolean: {bool_var} (Type: {type(bool_var)})")

# Function for arithmetic operations
def arithmetic_ops(a, b):
    print("\nArithmetic Operations:")
    print(f"Addition: {a} + {b} = {a + b}")
    print(f"Subtraction: {a} - {b} = {a - b}")
    print(f"Multiplication: {a} * {b} = {a * b}")
    print(f"Division: {b} / {a} = {b / a}")
    print(f"Modulus: {a} % 3 = {a % 3}")

# Function for string manipulations
def string_manipulation():
    greeting = "Hello"
    name = input("Enter your name: ")
    full_greeting = f"{greeting}, {name}!"
    
    print("\nString Manipulation:")
    print(full_greeting)

    str_var = "Hello, Main-Flow Technologies!"
    print(f"Formatted: {greeting}, {name}! Welcome to {str_var.split(',')[0]}.")
    print(f"Uppercase: {str_var.upper()}")
    print(f"Lowercase: {str_var.lower()}")
    print(f"Split: {str_var.split()}")

# Function for conditional statements

def conditional_statements(num):
    print("\nConditional Statements:")
    if num > 20:
        print(f"{num} is greater than 20.")
    elif num == 20:
        print(f"{num} is equal to 20.")
    else:
        print(f"{num} is less than 20.")

# Function for loops
def demonstrate_loops():
    print("\nFor Loop:")
    for i in range(5):
        print(f"Iteration {i}")

    print("\nWhile Loop:")
    count = 0
    while count < 5:
        print(f"Count: {count}")
        count += 1

# Function for basic arithmetic function examples

def basic_functions():
    def add(a, b):
        return a + b

    def greet(name):
        return f"Hello, {name}!"

    print("\nFunctions:")
    res = add(5, 7)
    print(f"Sum of 5 and 7: {res}")
    greet_msg = greet("Intern")
    print(greet_msg)

# Function to demonstrate data structures

def data_structures():
    fruits = ["apple", "banana", "cherry"]
    print("\nList:")
    print(f"Fruits: {fruits}")
    print(f"First Fruit: {fruits[0]}")

    person = {"name": "John", "age": 30, "city": "New York"}
    print("\nDictionary:")
    print(f"Person: {person}")
    print(f"Name: {person['name']}")

    colors = ("red", "green", "blue")
    print("\nTuple:")
    print(f"Colors: {colors}")
    print(f"First Color: {colors[0]}")



def main():
    display_var_types()
    
    a = int(input("Enter first number for arithmetic operations: "))
    b = float(input("Enter second number for arithmetic operations: "))
    arithmetic_ops(a, b)
    
    string_manipulation()
    
    num = int(input("Enter a number for conditional statements: "))
    conditional_statements(num)
    
    demonstrate_loops()
    basic_functions()
    data_structures()

    print("\nEnd of script. Python practice tasks completed.")

# Run the main function
if __name__ == "__main__":
    main()
