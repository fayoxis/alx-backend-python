#!/usr/bin/env python3
""" the below function’s parameters and return
values
"""
from typing import Sequence, Iterable, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Annotating the function """
    return [(i, len(i)) for i in lst]


if __name__ == '__main__':
    print(element_length.__annotations__)"
