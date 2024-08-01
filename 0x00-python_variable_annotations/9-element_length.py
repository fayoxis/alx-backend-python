#!/usr/bin/env python3
"""Module for calculating the length of sequences in a list."""


def element_length(sequences: list) -> list:
    """
    Compute the length of each sequence in the given list.

    Args:
        sequences (list): A list of sequences (e.g., strings, lists, tuples).

    Returns:
        list: A list of tuples, where each tuple contains the original sequence
              and its length.
    """
    return [(seq, len(seq)) for seq in sequences]
