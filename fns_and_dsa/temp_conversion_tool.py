"""
This module provides functions for converting temperatures between Celsius and Fahrenheit.
"""

FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5


def celsius_to_fahrenheit(celsius: float) -> float:
    """Converts a temperature from Celsius to Fahrenheit.

    Args:
        celsius: The temperature in Celsius.

    Returns:
        The temperature converted to Fahrenheit.
    """
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """Converts a temperature from Fahrenheit to Celsius.

    Args:
        fahrenheit: The temperature in Fahrenheit.

    Returns:
        The temperature converted to Celsius.
    """
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR


def get_user_input() -> tuple[float, str]:
    """Prompts the user for temperature and unit.

    Returns:
        A tuple containing the temperature (float) and unit ('C' or 'F').
    """
    while True:
        try:
            temperature = float(input("Enter the temperature to convert: "))
            unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper().strip()

            if unit not in ('C', 'F'):
                raise ValueError("Invalid unit. Please enter 'C' or 'F'.")

            return temperature, unit
        except ValueError as e:
            print(f"Error: {e}")


def main() -> None:
    """Main function to handle temperature conversion."""
    temperature, unit = get_user_input()

    if unit == 'C':
        converted_temp = celsius_to_fahrenheit(temperature)
        unit_label = '°C'
        converted_unit_label = '°F'
    else:
        converted_temp = fahrenheit_to_celsius(temperature)
        unit_label = '°F'
        converted_unit_label = '°C'

    print(f"{temperature}{unit_label} is {converted_temp:.2f}{converted_unit_label}")


if __name__ == "__main__":
    main()