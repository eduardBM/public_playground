"""
# UNLICENSE
Unittests for library puzzle2
Maintainer: Eduard Biceri-Matei (eduard.bicerimatei@gmail.com)

Documentation: see README.md
"""

import pytest

from puzzle2 import lib_puzzle2


def test_hp_first_ten():
    """
    Happy path: get 10 numbers, first one is 1 as string
    (!) Called function is a Generator
    """
    generator = lib_puzzle2.run(1, 10)
    values = list(generator)
    assert len(values) == 10
    assert values[0] == '1'


def test_hp_3_is_three():
    """
    Happy path: get number 3 as Three
    (!) Called function is a Generator
    """
    generator = lib_puzzle2.run(3, 3)
    values = list(generator)
    assert len(values) == 1
    assert values[0] == "Three"


def test_hp_5_is_five():
    """
    Happy path: get number 5 as Five
    (!) Called function is a Generator
    """
    generator = lib_puzzle2.run(5, 5)
    values = list(generator)
    assert len(values) == 1
    assert values[0] == "Five"


def test_hp_15_is_threefive():
    """
    Happy path: get number 15 as ThreeFive
    (!) Called function is a Generator
    """
    generator = lib_puzzle2.run(15, 15)
    values = list(generator)
    assert len(values) == 1
    assert values[0] == "ThreeFive"


def test_up_start_min():
    """
    UnHappy path: start < min
    (!) Called function is a Generator
    """
    with pytest.raises(ValueError):
        generator = lib_puzzle2.run(-1, 0)
        values = list(generator)


def test_up_end_max():
    """
    UnHappy path: end > max
    (!) Called function is a Generator
    """
    with pytest.raises(ValueError):
        generator = lib_puzzle2.run(0, lib_puzzle2.MAX_VAL+1)
        values = list(generator)


def test_up_not_an_int():
    """
    UnHappy path: values are not ints
    (!) Called function is a Generator
    """
    with pytest.raises(ValueError):
        generator = lib_puzzle2.run("0", "1")
        values = list(generator)


def test_up_wrong_order():
    """
    UnHappy path: end < start
    (!) Called function is a Generator
    """
    with pytest.raises(ValueError):
        generator = lib_puzzle2.run(1, 0)
        values = list(generator)
