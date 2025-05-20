"""
# UNLICENSE
Implementation library for puzzle3
validators

Maintainer: Eduard Biceri-Matei (eduard.bicerimatei@gmail.com)

Documentation: see README.md
"""

import string


def valid_int(value: str) -> int:
    """
    Checks if value is int
    returns as int
    raises ValueError
    """
    try:
        return int(value)
    except ValueError:
        raise ValueError(f"[valid_int/not_int] Value '{value}' is not an integer")


def valid_int_length(value: str, min_len: int = 0, max_len: int = 0) -> int:
    """
    Checks if value is int and min/max len as str
    returns as int
    raises ValueError
    """
    if not isinstance(value, str):
        raise ValueError(f"[valid_int_length/type] Value '{value}' has wrong type {type(value)}")
    if len(value) < min_len:
        raise ValueError(f"[valid_int_length/min] Value '{value}' must have {min_len} characters")
    if len(value) > max_len:
        raise ValueError(f"[valid_int_length/max] Value '{value}' must have {max_len} characters")
    return valid_int(value)


def valid_str_length_az(value: str, min_len: int = 0, max_len: int = 0):
    """
    Check if value is str, min/max len as str, A-Z only
    returns as str
    raises ValueError
    """
    if not isinstance(value, str):
        raise ValueError(f"[valid_str_length_az/type] Value '{value}' has wrong type {type(value)}")
    if len(value) < min_len:
        raise ValueError(f"[valid_str_length_az/min] Value '{value}' must have {min_len} characters")
    if len(value) > max_len:
        raise ValueError(f"[valid_str_length_az/max] Value '{value}' must have {max_len} characters")
    value = value.upper()
    for char in value:
        if char not in string.ascii_uppercase:
            raise ValueError(f"[valid_str_length_az/not_a_z] Value '{value}' contains invalid char {char}")
    return value


def valid_mix_int_str(value: str, min_len: int = 0, max_len: int = 0, str_len_at_end: int = 0) -> str:
    """
    Check if value is either [0-99] or [0-9][A-Z]
    returns as str
    raises ValueError
    """
    if str_len_at_end > max_len:
        raise ValueError(f"[WRONG_CALL] Invalid specification for `valid_mix_int_str`, {str_len_at_end=} > {max_len=} ")
    # check 1 or 2 digits
    if not isinstance(value, str):
        raise ValueError(f"[valid_mix_int_str/not_str] Value '{value}' has wrong type {type(value)}")
    try:
        return str(valid_int_length(value, min_len, max_len))
    except ValueError:
        # it's not a number
        # check last `str_len_at_end` characters at the end
        int_part = valid_int_length(value[:str_len_at_end], min_len=1, max_len=max_len-str_len_at_end)
        str_part = valid_str_length_az(value[str_len_at_end:], min_len=1, max_len=str_len_at_end)
        return f"{int_part}{str_part}"
