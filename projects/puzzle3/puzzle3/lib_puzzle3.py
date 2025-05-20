"""
# UNLICENSE
Implementation library for puzzle3
Maintainer: Eduard Biceri-Matei (eduard.bicerimatei@gmail.com)

Documentation: see README.md
"""

import string
from . import validators


class PostCodeUK:
    out_area = "<INVALID_OUT_AREA>"
    out_district = "<INVALID_OUT_DISTRICT>"
    in_sector = "<INVALID_IN_SECTOR>"
    in_unit = "<INVALID_IN_UNIT>"
    valid = False

    def __init__(self, out_area: str, out_district: str, in_sector: int, in_unit: str):
        """
        out_area: 1 or 2 A-Z a-z
        out_district: 1 or 2 digits, or 1 digit with 1 A-Z a-z
        in_sector: 1 digit
        in_unit: 2 chars
        """
        try:
            self.out_area = validators.valid_str_length_az(out_area, 1, 2)
            self.out_district = validators.valid_mix_int_str(out_district, 1, 2, 1)
            self.in_sector = validators.valid_int_length(in_sector, 1, 1)
            self.in_unit = validators.valid_str_length_az(in_unit, 2, 2)
            self.valid = True
        except ValueError as ve:
            raise ValueError(f"Could not validate PostCode: {self} {ve}")

    @classmethod
    def from_string(cls, value: str, strict=True):
        """
        Parse/Validate value to get a PostCodeUK
        if strict: must have spaces, all upper
        raise ValueError
        """
        if strict:
            if not isinstance(value, str):
                raise ValueError(f"[PostCodeUK] from_string (strict) invalid value {value}, must be string, not {type(value)}")
            if value.upper() != value:
                raise ValueError(f"[PostCodeUK] from_string (strict) invalid value {value}, must have all uppercases")
            if " " not in value:
                raise ValueError(f"[PostCodeUK] from_string (strict) invalid value {value}, must have a space")
            if any([char not in string.ascii_uppercase+string.digits+" " for char in value]):
                raise ValueError(f"[PostCodeUK] from_string (strict) invalid value {value}, must have all alphanumeric characters")

            if len(value) > 8:
                raise ValueError(f"[PostCodeUK] from_string (strict) invalid value {value}, value too long")
            if len(value) < 6:
                raise ValueError(f"[PostCodeUK] from_string (strict) invalid value {value}, value too short")
            # 3/4 space 3
            first_part, second_part = value.split(" ")
            if len(first_part) not in (2, 3, 4):
                raise ValueError(f"[PostCodeUK] from_string (strict) invalid value {value}, first part is invalid")
            if len(second_part) != 3:
                raise ValueError(f"[PostCodeUK] from_string (strict) invalid value {value}, second part is invalid")
            if first_part[1] in string.ascii_uppercase:
                # 2 char out_area
                out_area = first_part[:2]
                out_district = first_part[2:]
            else:
                # 1 char out_area
                out_area = first_part[:1]
                out_district = first_part[1:]
            in_sector = second_part[:1]
            in_unit = second_part[1:]
            return cls(out_area, out_district, in_sector, in_unit)
        else:
            # nothing to do here
            if not isinstance(value, str):
                raise ValueError(f"[PostCodeUK] from_string (strict) invalid value {value}, must be string, not {type(value)}")
            if any([char not in string.ascii_uppercase+string.ascii_lowercase+string.digits+" " for char in value]):
                raise ValueError(f"[PostCodeUK] from_string (strict) invalid value {value}, must have all alphanumeric characters")
            if len(value) > 8:
                raise ValueError(f"[PostCodeUK] from_string (strict) invalid value {value}, value too long")
            if len(value) < 6:
                raise ValueError(f"[PostCodeUK] from_string (strict) invalid value {value}, value too short")

            # fix missing space
            if " " not in value:
                first_part = value[:len(value)-3]
                second_part = value[len(value)-3:]
                value = f"{first_part} {second_part}"  # make sure it has a space
                try:
                    return cls.from_string(value, strict=True)
                except ValueError:
                    return cls.from_string(value, strict=False)  # try a different strategy
            # fix lowercase
            if value.upper() != value:
                try:
                    return cls.from_string(value.upper(), strict=True)
                except ValueError:
                    return cls.from_string(value.upper(), strict=False)  # try a different strategy

            # TODO: edge-cases, reformat before parsing ?
            try:
                return cls.from_string(value.upper(), strict=True)
            except ValueError:
                raise NotImplementedError("TODO: non-strict parsing from_string not implemented")

    def __str__(self):
        """
        Output as string, formatted
        """
        return f"{self.out_area}{self.out_district} {self.in_sector}{self.in_unit}"

    def __repr__(self):
        """
        Representation
        """
        return f"PostCodeUK('{self.out_area}', '{self.out_district}', '{self.in_sector}', '{self.in_unit}')"
