#!/usr/bin/env python3

"""module will annotates the variables"""

from typing import Union

def annotate_variables() -> None:
    a: int = 1
    pi: float = 3.14
    i_understand_annotations: bool = True
    school: str = 'Holberton'

    def print_variable(name: str, value: Union[int, float, bool, str]) -> None:
        print(f"{name} is a {type(value)} with a value of {value}")

    print_variable("a", a)
    print_variable("pi", pi)
    print_variable("i_understand_annotations", i_understand_annotations)
    print_variable("school", school)

if __name__ == '__main__':
    annotate_variables()
