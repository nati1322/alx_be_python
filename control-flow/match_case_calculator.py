def calculate(num1, num2, operation):
  """
  Performs the specified operation on the provided numbers.

  Args:
      num1: The first number.
      num2: The second number.
      operation: The operation to perform (+, -, *, /).

  Returns:
      The result of the operation or None if division by zero occurs.
  """
  match operation:
    case "+":
      return num1 + num2
    case "-":
      return num1 - num2
    case "*":
      return num1 * num2
    case "/":
      if num2 == 0:
        return None 
      else:
        return num1 / num2
    case _:
      return None 

if __name__ == "__main__":

  num1 = float(input("Enter the first number: "))
  num2 = float(input("Enter the second number: "))
  operation = input("Choose the operation (+, -, *, /): ")

  result = calculate(num1, num2, operation)

  if result is None:
    if operation == "/":
      print("Cannot divide by zero.")
    else:
      print("Invalid operation.")
  else:
    print(f"The result is {result}.")