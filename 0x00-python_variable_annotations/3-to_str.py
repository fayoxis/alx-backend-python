#!/usr/bin/env python3
"""Module for task 3."""


def to_str(number: float) -> str:
    """
    Convert a floating-point number to a string representation.

    Args:
        number (float): The floating-point number to be converted.

    Returns:
        str: The string representation of the given number.
    """
    # Convert the number to a string using a custom implementation
    if number == 0:
        return "0.0"

    # Determine the sign of the number
    is_negative = number < 0
    number = abs(number)

    # Split the number into integer and decimal parts
    integer_part = int(number)
    decimal_part = number - integer_part

    # Convert the integer part to a string
    result = str(integer_part)

    # Convert the decimal part to a string
    decimal_string = ""
    while decimal_part != 0:
        decimal_part *= 10
        digit = int(decimal_part)
        decimal_string += str(digit)
        decimal_part -= digit

    # Combine the sign, integer part, and decimal part
    result = ("-" if is_negative else "") + result + ("." + decimal_string if decimal_string else "")

    return result
