"""
# UNLICENSE
CLI helpers for Linux shells (mostly bash), using ANSI code
Might break Jenkins output or cli parser
Ask your entrypoint to disable colors
or invoke your library directly and output json

Maintainer: Eduard Biceri-Matei (eduard.bicerimatei@gmail.com)

Documentation: see README.md
"""

import datetime
import sys


def _level(level):
    levels = {
        "TRACE": f"\033[37m{level}\033[0m",  # WHITE
        "DEBUG": f"\033[34m{level}\033[0m",  # BLUE
        "INFO": f"\033[32m{level}\033[0m",  # GREEN
        "WARN": f"\033[33m{level}\033[0m",  # YELLOW
        "ERROR": f"\033[31m{level}\033[0m"  # RED
    }
    return levels.get(level, 'INFO')


def show(message, level="INFO", colors=True):
    now = datetime.datetime.now()
    if colors:
        print(f"[\033[32m{now}\033[0m][{_level(level)}] {message}", file=sys.stderr)
    else:
        print(f"[{now}][{level}] {message}")
