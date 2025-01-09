# This program converts temperatures between Celsius and Fahrenheit.

# These are special numbers that help us convert between Celsius and Fahrenheit.
celsius_to_fahrenheit_factor = 9 / 5
fahrenheit_to_celsius_factor = 5 / 9

# This function converts Celsius to Fahrenheit.
def convert_to_fahrenheit(celsius):
  """
  This function takes a temperature in Celsius and converts it to Fahrenheit.

  Args:
    celsius: The temperature in Celsius.

  Returns:
    The temperature in Fahrenheit.
  """
  fahrenheit = (celsius * celsius_to_fahrenheit_factor) + 32
  return fahrenheit

# This function converts Fahrenheit to Celsius.
def convert_to_celsius(fahrenheit):
  """
  This function takes a temperature in Fahrenheit and converts it to Celsius.

  Args:
    fahrenheit: The temperature in Fahrenheit.

  Returns:
    The temperature in Celsius.
  """
  celsius = (fahrenheit - 32) * fahrenheit_to_celsius_factor
  return celsius

# This part of the code asks the user for input and displays the result.
def main():
  while True:
    try:
      temperature = float(input("Enter the temperature to convert: ")) 
      unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper() 

      if unit == 'C':
        converted_temp = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {converted_temp:.2f}°F")
      elif unit == 'F':
        converted_temp = convert_to_celsius(temperature)
        print(f"{temperature}°F is {converted_temp:.2f}°C")
      else:
        print("Invalid unit. Please enter 'C' or 'F'.")
        continue  # Ask the user again if the unit is invalid

    except ValueError:
      print("Invalid input. Please enter a number for the temperature.")

if __name__ == "__main__":
  main()