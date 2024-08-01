#!/usr/bin/env python3
"""Contains Augmented code with the correct duck-typed annotations."""
from typing import Any, Union, Sequence


def safe_first_element(lst: Sequence) -> Union[Any, None]:
    """
    Return the first element of a sequence (list, tuple, etc.)
    or None if the sequence is empty.
    """
    if lst:
        return lst[0]
    else:
        return None
