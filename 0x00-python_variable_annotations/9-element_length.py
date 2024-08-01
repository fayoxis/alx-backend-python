#!/usr/bin/env python3
"""Module for computing the length of sequences in a list."""


def element_length(sequences: list) -> list:
    """
    Compute the length of each sequence in a list of sequences.

    Args:
        sequences (list): A list of sequences (e.g., lists, tuples, strings).

    Returns:
        list: A list of tuples, where each tuple contains the original sequence
        and its length.
    """
    lengths = []
    for seq in sequences:
        lengths.append((seq, len(seq)))
    return lengths
