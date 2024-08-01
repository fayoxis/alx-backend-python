#!/usr/bin/env python3
"""
A function with annotated parameters and
return values using appropriate types.
"""
from typing import Iterable, Sequence, List, Tuple


def get_sequence_lengths(sequences: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples containing each sequence and its length.

    Args:
        sequences (Iterable[Sequence]): An iterable of sequences.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples, where each tuple contains
            a sequence and its length.
    """
    return [(seq, len(seq)) for seq in sequences]
