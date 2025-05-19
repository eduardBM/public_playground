"""
# UNLICENSE
Implementation library for puzzle2
Maintainer: Eduard Biceri-Matei (eduard.bicerimatei@gmail.com)

Documentation: see README.md
"""

from typing import Generator

# CONSTANTS
MIN_VAL = 0
MAX_VAL = 100


def _valid_int(value: int, var_name: str):
    if not isinstance(value, int):
        raise ValueError(f"Unexpected value for {var_name}: {value} {type(value)}")
    if value < MIN_VAL or value > MAX_VAL:
        raise ValueError(f"Expected value for {var_name} to be between {MIN_VAL} and {MAX_VAL}")


def run(start_val: int = MIN_VAL, end_val: int = MAX_VAL) -> Generator[str, None, None]:
    """
    Yields numbers from 1 to 100
    for multiples of three yields “Three” instead of the number
    for the multiples of five yields “Five”.
    for numbers which are multiples of both three and yields print “ThreeFive”.
    """

    _valid_int(start_val, 'start_val')
    _valid_int(end_val, 'end_val')
    if end_val < start_val:
        raise ValueError(f"End val is smaller than start val")
    for number in range(start_val, end_val+1):
        if number % 15 == 0:
            yield "ThreeFive"
        elif number % 3 == 0:
            yield "Three"
        elif number % 5 == 0:
            yield "Five"
        else:
            yield str(number)
