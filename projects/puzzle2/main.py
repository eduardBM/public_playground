"""
# UNLICENSE

Main CLI script for puzzle2
requires lib_puzzle2

Maintainer: Eduard Biceri-Matei (eduard.bicerimatei@gmail.com)

Documentation: see README.md
"""

import argparse
import time

from cli_helpers.colors import show
from puzzle2 import lib_puzzle2


def main(start_val: int, end_val: int, colors: bool = True) -> None:
    show(f"Puzzle2 running {start_val} {end_val}", "INFO", colors)
    for value in lib_puzzle2.run(start_val, end_val):
        print(value)  # actual values go directly to stdout, cli_helpers goes to stderr


if __name__ == "__main__":
    parser = argparse.ArgumentParser(__file__, __doc__)
    parser.add_argument("start_val", type=int, help="Start value")
    parser.add_argument("end_val", type=int, help="End value")
    parser.add_argument("--time", default=False, help="Show timing", action='store_true')
    parser.add_argument("--disable_colors", default=False, help="Disable ANSI colors in output", action='store_true')

    args = parser.parse_args()
    colors = not args.disable_colors
    if args.time:
        start = time.time()

    try:
        main(args.start_val, args.end_val)
    except ValueError as ve:
        show(f"Error during execution", "ERROR", colors)
    if args.time:
        end = time.time()
        show(f"Execution took {(end-start):.4f} seconds", "INFO", colors)
