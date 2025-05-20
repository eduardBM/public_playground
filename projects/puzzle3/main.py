"""
# UNLICENSE

Main CLI script for puzzle3
requires lib_puzzle3

Maintainer: Eduard Biceri-Matei (eduard.bicerimatei@gmail.com)

Documentation: see README.md
"""

import argparse
import time

from cli_helpers.colors import show
from puzzle3 import lib_puzzle3


def main(code: str, strict: bool = False, colors: bool = True) -> None:
    show(f"Puzzle3 running ", "INFO", colors)
    # impl
    postcode_UK = lib_puzzle3.PostCodeUK.from_string(code, strict=strict)
    print(postcode_UK)
    print(postcode_UK.valid)
    print(repr(postcode_UK))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(__file__, __doc__)
    parser.add_argument("code", type=str, help="Code to validate")
    parser.add_argument("--strict", default=False, help="Use strict mode (experimental)", action='store_true')

    parser.add_argument("--time", default=False, help="Show timing", action='store_true')
    parser.add_argument("--disable_colors", default=False, help="Disable ANSI colors in output", action='store_true')

    args = parser.parse_args()
    colors = not args.disable_colors
    if args.time:
        start = time.time()

    try:
        main(args.code, args.strict, colors)
    except ValueError as ve:
        show(f"Error during execution: {ve}", "ERROR", colors)
    if args.time:
        end = time.time()
        show(f"Execution took {(end-start):.4f} seconds", "INFO", colors)
