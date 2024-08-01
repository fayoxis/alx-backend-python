#!/usr/bin/env python3
"""Task 2's module."""


def floor(number: float) -> int:
    """
    Computes the floor of a floating-point number.

    Args:
        number (float): The floating-point number to find the floor of.

    Returns:
        int: The floor of the given number.
    """
    # Convert the float to an integer by truncating the decimal part
    integer_part = int(number)

    # If the number is negative and has a non-zero decimal part,
    # subtract 1 from the integer part to get the floor
    if number < 0 and number != integer_part:
        integer_part -= 1

    return integer_part
