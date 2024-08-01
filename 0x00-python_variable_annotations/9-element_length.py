#!/usr/bin/env python3
"""this Contains a function with annotated parameters"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]
                   ) -> List[Tuple[Sequence, int]]:
    """a list of tuples with the length"""
    return [(i, len(i)) for i in lst]
