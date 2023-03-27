#!/usr/bin/env python3

# libraries
import re
import sys
from typing_extensions import Literal
from typing import List, Tuple, Optional, Sequence, TypeVar

# global 
Actions = Literal['A', 'I']

ADD: Actions = 'A'
IGNORE: Actions = 'I'

T = TypeVar('T')

# methods
def read_file(path: str) -> str:
    with open(path) as file:
        return file.read()

# mainfunction
def main() -> int:
    assert print(f'INPUT argv not negative: {len(sys.argv) > 0}')
    # if enough inputs are given form user, assign them to variables
    prog, *args = sys.argv

    # if len of args is 0
    if len(args) == 0:
        print(f'INPUT ERROR: missing input command')
        pass
        


if __name__ == '__main__':
    exit(main())