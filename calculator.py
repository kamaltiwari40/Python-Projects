def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero."
    return x / y

ops = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

num1 = float(input("Enter a Number: "))
op = input("Enter a operator (+, -, *, /): ")
num2 = float(input("Enter a Number: "))

if op in ops:
    print(f"{num1}, {op} {num2}, {ops[op](num1, num2)}")
    
else:
    print("invalid input")