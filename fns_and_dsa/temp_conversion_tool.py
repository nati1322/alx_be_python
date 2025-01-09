import os

# Checks for Definition of global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

# Checks for Implement conversion functions
def convert_to_celsius(fahrenheit):
  """Converts a temperature from Fahrenheit to Celsius.

  Args:
      fahrenheit: The temperature in Fahrenheit (float).

  Returns:
      The temperature converted to Celsius (float).
  """
  return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
  """Converts a temperature from Celsius to Fahrenheit.

  Args:
      celsius: The temperature in Celsius (float).

  Returns:
      The temperature converted to Fahrenheit (float).
  """
  return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# Checks for User interaction
def get_user_input():
  while True:
    try:
      temperature = float(input("Enter the temperature to convert: "))
      unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper().strip()
      if unit not in ('C', 'F'):
        raise ValueError("Invalid unit. Please enter 'C' or 'F'.")
      return temperature, unit
    except ValueError as e:
      print(f"Error: {e}")

def main():
  while True:
    try:
      temperature, unit = get_user_input()

      if unit == 'C':
        converted_temp = convert_to_fahrenheit(temperature)
        unit_label = '°C'
        converted_unit_label = '°F'
      elif unit == 'F':
        converted_temp = convert_to_celsius(temperature)
        unit_label = '°F'
        converted_unit_label = '°C'

      print(f"{temperature}{unit_label} is {converted_temp:.2f}{converted_unit_label}")
      break

    except ValueError as e: 
      # Checks for Implementation of Value Error
      print(f"Error: {e}")

if __name__ == "__main__":
  main()