# Define global conversion factors within a class
class ConversionFactors:
    FAHRENHEIT_TO_CELSIUS = 5 / 9
    CELSIUS_TO_FAHRENHEIT = 9 / 5

def convert_to_celsius(fahrenheit):
  """Converts a temperature from Fahrenheit to Celsius.

  Args:
      fahrenheit: The temperature in Fahrenheit (float).

  Returns:
      The temperature converted to Celsius (float).
  """
  return (fahrenheit - 32) * ConversionFactors.FAHRENHEIT_TO_CELSIUS

def convert_to_fahrenheit(celsius):
  """Converts a temperature from Celsius to Fahrenheit.

  Args:
      celsius: The temperature in Celsius (float).

  Returns:
      The temperature converted to Fahrenheit (float).
  """
  return (celsius * ConversionFactors.CELSIUS_TO_FAHRENHEIT) + 32

def main():
  while True:
    try:
      temperature = float(input("Enter the temperature to convert: "))
      unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper().strip()

      if unit == 'C':
        converted_temp = convert_to_fahrenheit(temperature)
        unit_label = '°C'
        converted_unit_label = '°F'
      elif unit == 'F':
        converted_temp = convert_to_celsius(temperature)
        unit_label = '°F'
        converted_unit_label = '°C'
      else:
        raise ValueError("Invalid unit. Please enter 'C' or 'F'.")

      print(f"{temperature}{unit_label} is {converted_temp:.2f}{converted_unit_label}")
      break

    except ValueError as e:
      print(f"Error: {e}")

if __name__ == "__main__":
  main()