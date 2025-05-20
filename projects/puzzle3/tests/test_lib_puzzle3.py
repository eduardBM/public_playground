"""
# UNLICENSE
Unittests for library puzzle3
Maintainer: Eduard Biceri-Matei (eduard.bicerimatei@gmail.com)

Documentation: see README.md
"""

import pytest

from puzzle3 import lib_puzzle3


# Test data
def postcode_valid_formats():
    return [
        ("AA", "99", "9", "AA"),
        ("AA", "9", "9", "AA"),
        ("A", "9", "9", "AA"),
        ("A", "99", "9", "AA"),
        ("A", "9A", "9", "AA"),
        ("AA", "9A", "9", "AA"),
    ]


def postcode_invalid_formats():
    return [
        (None, None, None, None),
        ("AA", None, None, None),
        ("AA", "99", None, None),
        ("AA", "99", "9", None),
        ("", "", "", ""),
        ("AA", "", "", ""),
        ("AA", "99", "", ""),
        ("AA", "99", "9", ""),
        ("AA", "99", -1, "AA"),
    ]


def postcode_valid_strings():
    return [
        "AA99 9AA",
        "AA9 9AA",
        "A9 9AA",
        "A99 9AA",
        "A9A 9AA",
        "AA9A 9AA",
    ]


def postcode_invalid_strings():
    return [
        "a",
        " ",
        "9",
        9,
        "_ 9AA",
        "AA9999AA",
        "9AA 9AA",
        "AA9 9A",
        "99A 9AA",
        "A9A 99A",
        "A 99 9AA",
        "A 999AA",
        "AA99 99AA",
        "aa99 99a a",
        "a1199aa"
    ]


def postcode_invalid_strings_fixable():
    return [
        "aa19aa",
        "aa12 9aa",
        "AA999AA",
    ]
# ("SW", "1W", "0", "NY")


@pytest.mark.parametrize("postcode_valid_format", postcode_valid_formats())
def test_hp_valid_formats(postcode_valid_format):
    """
    Happy path: valid formats, no exception raised
    """
    postcode_UK = lib_puzzle3.PostCodeUK(*postcode_valid_format)
    assert postcode_UK.valid


@pytest.mark.parametrize("postcode_invalid_format", postcode_invalid_formats())
def test_up_invalid_formats(postcode_invalid_format):
    """
    Unhappy path: invalid formats, ValueError raised
    """
    with pytest.raises(ValueError):
        _ = lib_puzzle3.PostCodeUK(*postcode_invalid_format)


@pytest.mark.parametrize("postcode_valid_string", postcode_valid_strings())
def test_hp_valid_strings(postcode_valid_string):
    """
    Happy path: valid string, no exception raised
    """
    postcode_UK = lib_puzzle3.PostCodeUK.from_string(postcode_valid_string)
    assert postcode_UK.valid


@pytest.mark.parametrize("postcode_invalid_string", postcode_invalid_strings())
def test_up_invalid_strings(postcode_invalid_string):
    """
    Unhappy path: invalid string, ValueError raised
    """
    with pytest.raises(ValueError):
        _ = lib_puzzle3.PostCodeUK.from_string(postcode_invalid_string)


@pytest.mark.parametrize("postcode_invalid_string", postcode_invalid_strings())
def test_up_invalid_strings_non_strict(postcode_invalid_string):
    """
    Unhappy path: invalid string, try to fix unfixable
    """
    with pytest.raises((ValueError, NotImplementedError)):
        _ = lib_puzzle3.PostCodeUK.from_string(postcode_invalid_string, strict=False)


@pytest.mark.parametrize("postcode_invalid_string_fixable", postcode_invalid_strings_fixable())
def test_hp_invalid_strings_non_strict_fixable(postcode_invalid_string_fixable):
    """
    Happy path: invalid string, try to fix fixable
    """
    postcode_UK = lib_puzzle3.PostCodeUK.from_string(postcode_invalid_string_fixable, strict=False)
    assert postcode_UK.valid
