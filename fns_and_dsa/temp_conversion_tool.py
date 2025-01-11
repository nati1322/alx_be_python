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
        user_input = input("Enter the temperature to convert (or 'q' to quit): ")
        if user_input.lower() == 'q':
            break

        # Directly convert input to float, catching any non-numeric errors
        input_temperature = float(user_input)

        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()

        if unit not in ("C", "F"):
            print("Invalid input: Please enter 'C' or 'F'.")
            continue

        if unit == "C":
            output_temperature = convert_to_fahrenheit(input_temperature)
            print(f"{input_temperature:.1f}°C is {output_temperature:.1f}°F")
        elif unit == "F":
            output_temperature = convert_to_celsius(input_temperature)
            print(f"{input_temperature:.1f}°F is {output_temperature:.1f}°C")
        break

    except ValueError:  # Now catches any conversion error
        print("Invalid input: Please enter a valid temperature.")
        continue