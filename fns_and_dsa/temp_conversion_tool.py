# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    """Converts Fahrenheit to Celsius using the global factor."""
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    """Converts Celsius to Fahrenheit using the global factor."""
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

while True:
    try:
        user_input = input("Enter the temperature to convert: ")
        temperature_value = float(user_input)

        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()

        if unit not in ("C", "F"):
            raise ValueError("Invalid unit. Please enter 'C' or 'F'.")

        if unit == "C":
            converted_temp = convert_to_fahrenheit(temperature_value)
            print(f"{temperature_value:.1f}°C is {converted_temp:.1f}°F")
        elif unit == "F":
            converted_temp = convert_to_celsius(temperature_value)
            print(f"{temperature_value:.1f}°F is {converted_temp:.1f}°C")
        break

    except ValueError as e:
        print(f"Invalid input: {e}")