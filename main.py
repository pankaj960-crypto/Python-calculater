print("Calculator")

def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y


def divide(x,y):
    return x / y

operation = {
          "+": add,
          "-": subtract,
          "*": multiply,
          "/": divide
}
try:
          num1 = float(input("Enter first number:"))

          for symbol in operation:
              print(symbol)
          operation_symbol = input("Enter operation: ")
          num2 = float(input("Enter second number: "))
          if operation_symbol in operation:
             answer = operation[operation_symbol](num1, num2)
             print(f"{num1} {operation_symbol} {num2} = {answer}")
          else:
             print("Invalid operation")
except ValueError:
      print("Invalid input:")

while True:
      should_continue = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")
      if should_continue == "y":
          num1 = answer
          for symbol in operation:
              print(symbol)
          operation_symbol = input("choose an operation: ")
          num2 = float(input("Enter second number: "))
          if operation_symbol in operation:
              answer = operation[operation_symbol](num1, num2)
              print(f"{num1} {operation_symbol} {num2} = {answer}")
          else:
              print("Invalid operation")
      else:
          break